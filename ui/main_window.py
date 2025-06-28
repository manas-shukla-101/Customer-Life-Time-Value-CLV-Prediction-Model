import tkinter as tk
from tkinter import ttk, messagebox
from utils.logger import get_logger

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Customer Life-Time Value Prediction")
        self.geometry("1200x800")
        self.minsize(1000, 600)
        
        # Initialize core components
        self.logger = get_logger("MainApplication")
        self.df = None
        self.rfm_data = None
        self.model = None
        
        # UI Setup
        self._setup_ui()
        self.update_status("Ready")
        self.feature_importance = None

    def _setup_ui(self):
        """Initialize all UI components."""
        # Configure styles
        self.style = ttk.Style()
        self.style.configure('Header.TLabel', font=('Arial', 12, 'bold'))
        
        # Create container
        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        
        # Initialize panels
        from ui.data_panel import DataPanel
        from ui.analysis_panel import AnalysisPanel
        from ui.results_panel import ResultsPanel
        
        self.frames = {}
        for F in (DataPanel, AnalysisPanel, ResultsPanel):
            frame = F(container, self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        # Navigation
        nav_frame = ttk.Frame(self)
        nav_frame.pack(side="top", fill="x")
        ttk.Button(nav_frame, text="Data", command=lambda: self.show_frame("DataPanel")).pack(side="left")
        ttk.Button(nav_frame, text="Analysis", command=lambda: self.show_frame("AnalysisPanel")).pack(side="left")
        ttk.Button(nav_frame, text="Results", command=lambda: self.show_frame("ResultsPanel")).pack(side="left")
        
        # Status bar
        self.status_var = tk.StringVar()
        ttk.Label(self, textvariable=self.status_var, relief="sunken").pack(side="bottom", fill="x")
        
        self.show_frame("DataPanel")

    def show_frame(self, name):
        """Show a frame by name."""
        frame = self.frames[name]
        frame.tkraise()
        self.update_status(f"Showing {name.replace('Panel', '')} panel")

    def update_status(self, message):
        """Update status bar safely."""
        if hasattr(self, 'status_var'):
            self.status_var.set(message[:100])  # Limit length
            self.logger.info(message)

    def show_error(self, title, message):
        """Show error dialog safely."""
        try:
            messagebox.showerror(title, message)
            self.update_status(f"Error: {message}")
            self.logger.error(f"{title}: {message}")
        except Exception as e:
            print(f"Error display failed: {e}")