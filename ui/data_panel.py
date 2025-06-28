import tkinter as tk
from tkinter import ttk, filedialog
from utils.helpers import safe_str
from utils.logger import get_logger

logger = get_logger(__name__)

class DataPanel(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self._setup_ui()
    
    def _setup_ui(self):
        """Initialize UI components."""
        ttk.Label(self, text="Data Loading", style="Header.TLabel").pack(pady=10)
        
        # Main content
        content = ttk.Frame(self)
        content.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Data source controls
        source_frame = ttk.LabelFrame(content, text="Data Source", padding=10)
        source_frame.pack(fill="x", pady=5)
        
        ttk.Button(source_frame, text="Load CSV", command=self._load_csv).pack(side="left", padx=5)
        ttk.Button(source_frame, text="Use Sample Data", command=self._use_sample).pack(side="left", padx=5)
        ttk.Button(source_frame, text="View Data", command=self._view_data).pack(side="left", padx=5)
        
        # Data info display
        info_frame = ttk.LabelFrame(content, text="Data Information", padding=10)
        info_frame.pack(fill="both", expand=True)
        
        self.info_text = tk.Text(info_frame, wrap="word", state="disabled")
        scroll = ttk.Scrollbar(info_frame, command=self.info_text.yview)
        self.info_text.config(yscrollcommand=scroll.set)
        
        scroll.pack(side="right", fill="y")
        self.info_text.pack(fill="both", expand=True)
    
    def _load_csv(self):
        """Handle CSV file loading."""
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if not file_path:
            return
            
        try:
            from data.loader import load_raw_data
            self.controller.df = load_raw_data(file_path)
            
            if self.controller.df is not None:
                self._show_info(f"Loaded {len(self.controller.df)} records")
                self.controller.update_status("Data loaded successfully")
            else:
                self.controller.show_error("Loading Failed", "Could not load data")
        except Exception as e:
            self.controller.show_error("Loading Error", safe_str(e))
    
    def _use_sample(self):
        """Handle sample data generation."""
        try:
            from data.loader import create_sample_data
            self.controller.df = create_sample_data()
            self._show_info(f"Generated {len(self.controller.df)} sample records")
            self.controller.update_status("Sample data ready")
        except Exception as e:
            self.controller.show_error("Sample Error", safe_str(e))
    
    def _view_data(self):
        """Display data preview."""
        if not hasattr(self.controller, 'df') or self.controller.df is None:
            self.controller.show_error("No Data", "Please load data first")
            return
            
        # Create preview window
        preview = tk.Toplevel(self)
        preview.title("Data Preview")
        
        # Create treeview
        tree = ttk.Treeview(preview)
        tree.pack(fill="both", expand=True)
        
        # Add columns
        tree["columns"] = list(self.controller.df.columns)
        for col in self.controller.df.columns:
            tree.heading(col, text=col)
        
        # Add sample rows
        for _, row in self.controller.df.head(100).iterrows():
            tree.insert("", "end", values=list(row))
    
    def _show_info(self, message):
        """Update info display."""
        self.info_text.config(state="normal")
        self.info_text.delete(1.0, "end")
        self.info_text.insert("end", message)
        self.info_text.config(state="disabled")