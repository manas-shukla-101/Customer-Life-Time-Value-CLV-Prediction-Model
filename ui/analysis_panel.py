import tkinter as tk
from tkinter import ttk
from utils.helpers import safe_str
from utils.logger import get_logger

logger = get_logger(__name__)

class AnalysisPanel(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self._setup_ui()
    
    def _setup_ui(self):
        """Initialize UI components."""
        ttk.Label(self, text="Data Analysis", style="Header.TLabel").pack(pady=10)
        
        # Analysis controls
        controls = ttk.Frame(self)
        controls.pack(fill="x", padx=10, pady=5)
        
        ttk.Button(controls, text="Clean Data", command=self._clean_data).pack(side="left", padx=5)
        ttk.Button(controls, text="Calculate RFM", command=self._calculate_rfm).pack(side="left", padx=5)
        ttk.Button(controls, text="Train Model", command=self._train_model).pack(side="left", padx=5)
        
        # Results display
        results = ttk.LabelFrame(self, text="Analysis Results", padding=10)
        results.pack(fill="both", expand=True, padx=10, pady=5)
        
        self.results_text = tk.Text(results, wrap="word", state="disabled")
        scroll = ttk.Scrollbar(results, command=self.results_text.yview)
        self.results_text.config(yscrollcommand=scroll.set)
        
        scroll.pack(side="right", fill="y")
        self.results_text.pack(fill="both", expand=True)
    
    def _clean_data(self):
        """Clean the loaded data."""
        if not hasattr(self.controller, 'df') or self.controller.df is None:
            self.controller.show_error("No Data", "Please load data first")
            return
            
        try:
            from data.cleaner import clean_data
            self.controller.df = clean_data(self.controller.df)
            self._log_result("Data cleaned successfully")
            self.controller.update_status("Data cleaning complete")
        except Exception as e:
            self.controller.show_error("Cleaning Error", safe_str(e))
    
    def _calculate_rfm(self):
        """Enhanced RFM calculation with better feedback."""
        if not hasattr(self.controller, 'df') or self.controller.df is None:
            self.controller.show_error("No Data", "Please load and clean data first")
            return
        
        try:
            from features.rfm import calculate_rfm
            from visualization.plots import generate_rfm_plots
            
            self._log_result("\nStarting RFM analysis...")
            self.update()  # Force UI update
            
            # Step 1: Calculate RFM metrics
            self.controller.rfm_data = calculate_rfm(self.controller.df)
            
            if self.controller.rfm_data is None:
                self._log_result("RFM calculation failed")
                return
                
            self._log_result(f"Calculated RFM for {len(self.controller.rfm_data)} customers")
            
            # Step 2: Generate visualizations
            self._log_result("Generating visualizations...")
            success = generate_rfm_plots(self.controller.rfm_data)
            
            if success:
                self._log_result("Visualizations generated successfully")
                self.controller.update_status("RFM analysis complete - check Results tab")
            else:
                self._log_result("Warning: Visualization generation failed")
                self.controller.show_error(
                    "Visualization Error",
                    "RFM metrics calculated but visualizations failed\n" +
                    "Check logs for details"
                )
                
        except Exception as e:
            error_msg = safe_str(e)
            self._log_result(f"Error: {error_msg}")
            self.controller.show_error("RFM Analysis Failed", error_msg)
    
    def _train_model(self):
        """Train predictive model."""
        if not hasattr(self.controller, 'rfm_data') or self.controller.rfm_data is None:
            self.controller.show_error("No RFM Data", "Please calculate RFM metrics first")
            return
            
        try:
            from models.trainer import train_model, prepare_data
            X_train, _, y_train, _, _ = prepare_data(self.controller.rfm_data)
            self.controller.model = train_model(X_train, y_train)
            
            if self.controller.model is not None:
                self._log_result("Model trained successfully")
                self.controller.update_status("Model training complete")
            else:
                self.controller.show_error("Training Error", "Model training failed")
                
        except Exception as e:
            self.controller.show_error("Training Error", safe_str(e))
    
    def _log_result(self, message):
        """Add message to results log."""
        self.results_text.config(state="normal")
        self.results_text.insert("end", message + "\n")
        self.results_text.config(state="disabled")
        self.results_text.see("end")