import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
from config import OUTPUT_DIR
from utils.logger import get_logger
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

logger = get_logger(__name__)

class ResultsPanel(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.image_references = []  # To prevent garbage collection
        self._setup_ui()
    
    def _setup_ui(self):
        """Initialize all UI components."""
        ttk.Label(self, text="Analysis Results", style="Header.TLabel").pack(pady=10)
        
        # Notebook for multiple visualizations
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Create visualization tabs
        self._create_viz_tab("RFM Analysis", "rfm_distributions.png")
        self._create_viz_tab("Feature Importance", "feature_importance.png")
        self._create_segmentation_tab()
        
        # Add export controls
        self._setup_export_controls()
        
        # Refresh button
        ttk.Button(self, text="Refresh Visualizations", command=self._refresh_visualizations).pack(pady=5)

    def _create_viz_tab(self, name, image_file):
        """Create a tab for visualization."""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text=name)
        
        # Canvas for image
        canvas = tk.Canvas(tab)
        canvas.pack(fill="both", expand=True)
        
        # Initial image load
        self._load_image(tab, os.path.join(OUTPUT_DIR, image_file))

    def _create_segmentation_tab(self):
        """Add customer segmentation visualization tab."""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Segmentation")
        
        # Segmentation controls
        control_frame = ttk.Frame(tab)
        control_frame.pack(fill="x", padx=5, pady=5)
        
        ttk.Label(control_frame, text="Segment By:").pack(side="left")
        self.segment_var = tk.StringVar(value="CLV")
        ttk.OptionMenu(
            control_frame, 
            self.segment_var, 
            "CLV", 
            "Recency", 
            "Frequency", 
            "Monetary"
        ).pack(side="left")
        
        ttk.Button(
            control_frame, 
            text="Generate", 
            command=self._update_segmentation
        ).pack(side="left", padx=5)
        
        # Visualization canvas
        self.segmentation_canvas = FigureCanvasTkAgg(plt.Figure(figsize=(10,6)), master=tab)
        self.segmentation_canvas.get_tk_widget().pack(fill="both", expand=True)
        self._update_segmentation()

    def _update_segmentation(self):
        """Update segmentation visualization."""
        if not hasattr(self.controller, 'rfm_data'):
            return
            
        fig = self.segmentation_canvas.figure
        fig.clear()
        ax = fig.add_subplot(111)
        segment_by = self.segment_var.get()
        
        try:
            sns.boxplot(
                x='Segment',
                y=segment_by,
                data=self.controller.rfm_data,
                ax=ax,
                palette="Set3"
            )
            ax.set_title(f"Customer Segmentation by {segment_by}")
            ax.tick_params(axis='x', rotation=45)
            self.segmentation_canvas.draw()
        except Exception as e:
            ax.text(0.5, 0.5, "Segmentation data not available", ha="center")
            self.segmentation_canvas.draw()
            logger.error(f"Segmentation error: {e}")

    def _setup_export_controls(self):
        """Add export buttons to each tab."""
        for tab_id in self.notebook.tabs():
            tab = self.notebook.nametowidget(tab_id)
            
            export_frame = ttk.Frame(tab)
            export_frame.pack(side="bottom", fill="x", pady=5)
            
            ttk.Button(
                export_frame,
                text="Export as PNG",
                command=lambda t=tab_id: self._export_as_image(t)
            ).pack(side="left", padx=5)
            
            ttk.Button(
                export_frame,
                text="Export Data",
                command=lambda t=tab_id: self._export_as_csv(t)
            ).pack(side="left")

    def _load_image(self, parent, image_path):
        """Load and display an image with error handling."""
        # Clear previous widgets
        for widget in parent.winfo_children():
            widget.destroy()
        
        # Check if image exists
        if not os.path.exists(image_path):
            ttk.Label(parent, 
                    text=f"Visualization not found:\n{os.path.basename(image_path)}",
                    justify="center").pack(expand=True)
            return
        
        try:
            # Load and resize image
            img = Image.open(image_path)
            img = img.resize((800, 400), Image.LANCZOS)
            tk_img = ImageTk.PhotoImage(img)
            
            # Keep reference to prevent garbage collection
            self.image_references.append(tk_img)
            
            # Display image
            label = ttk.Label(parent, image=tk_img)
            label.pack(fill="both", expand=True)
            
        except Exception as e:
            ttk.Label(parent, 
                    text=f"Error loading visualization:\n{str(e)}",
                    justify="center").pack(expand=True)
            logger.error(f"Error loading {image_path}: {e}")

    def _refresh_visualizations(self):
        """Reload all visualization images."""
        self.image_references.clear()  # Clear old references
        
        for tab_id in self.notebook.tabs():
            tab = self.notebook.nametowidget(tab_id)
            tab_name = self.notebook.tab(tab_id, "text")
            
            # Determine which image to load based on tab name
            image_file = ""
            if "RFM" in tab_name:
                image_file = "rfm_distributions.png"
            elif "Feature" in tab_name:
                image_file = "feature_importance.png"
            
            if image_file:
                self._load_image(tab, os.path.join(OUTPUT_DIR, image_file))
        
        self.controller.update_status("Visualizations refreshed")

    def _export_as_image(self, tab_id):
        """Export visualization as image."""
        tab_name = self.notebook.tab(tab_id, "text")
        tab = self.notebook.nametowidget(tab_id)
        
        # Find visualization canvas
        for widget in tab.winfo_children():
            if isinstance(widget, FigureCanvasTkAgg):
                fig = widget.figure
                export_path = os.path.join(OUTPUT_DIR, f"{tab_name.replace(' ', '_')}.png")
                fig.savefig(export_path, dpi=300, bbox_inches='tight')
                self.controller.update_status(f"Exported {tab_name} to {export_path}")
                return
        
        self.controller.show_error("Export Failed", "No visualization found to export")

    def _export_as_csv(self, tab_id):
        """Export underlying data as CSV."""
        tab_name = self.notebook.tab(tab_id, "text")
        export_path = os.path.join(OUTPUT_DIR, f"{tab_name.replace(' ', '_')}.csv")
        
        try:
            if hasattr(self.controller, 'rfm_data'):
                if tab_name == "Segmentation":
                    self.controller.rfm_data.to_csv(export_path, index=False)
                elif tab_name == "Feature Importance" and hasattr(self.controller, 'feature_importance'):
                    self.controller.feature_importance.to_csv(export_path, index=False)
                else:
                    raise ValueError("No exportable data for this tab")
                
                self.controller.update_status(f"Exported {tab_name} data to {export_path}")
            else:
                raise ValueError("No analysis data available")
        except Exception as e:
            self.controller.show_error("Export Failed", str(e))
            logger.error(f"Export failed: {e}")