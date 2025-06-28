import matplotlib
matplotlib.use('Agg')  # Set non-interactive backend
import matplotlib.pyplot as plt
import seaborn as sns
import os
from config import OUTPUT_DIR
from utils.logger import get_logger

logger = get_logger(__name__)

def generate_rfm_plots(rfm_data):
    """Generate and save RFM visualization plots."""
    try:
        # Ensure output directory exists
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        
        # Set style with fallback
        try:
            plt.style.use('seaborn-v0_8')  # Modern seaborn style
        except:
            plt.style.use('ggplot')  # Fallback style
        
        # Create figure with subplots
        fig, axes = plt.subplots(1, 3, figsize=(18, 6))
        
        # Plot 1: Monetary Distribution
        sns.histplot(
            rfm_data['Monetary'], 
            bins=30, 
            kde=True, 
            ax=axes[0],
            color='skyblue'
        )
        axes[0].set_title('Customer Spending', fontweight='bold')
        axes[0].set_xlabel('Total Spend ($)', fontsize=9)
        
        # Plot 2: Frequency vs Recency
        sns.scatterplot(
            x='Recency',
            y='Frequency',
            size='Monetary',
            sizes=(20, 200),
            alpha=0.7,
            palette='viridis',
            data=rfm_data,
            ax=axes[1]
        )
        axes[1].set_title('Purchase Pattern', fontweight='bold')
        
        # Plot 3: CLV Distribution
        sns.boxplot(
            y=rfm_data['CLV'],
            ax=axes[2],
            color='lightgreen'
        )
        axes[2].set_title('Customer Value', fontweight='bold')
        
        plt.tight_layout(pad=2.0)
        
        # Save figure
        output_path = os.path.join(OUTPUT_DIR, 'rfm_distributions.png')
        fig.savefig(
            output_path,
            dpi=120,
            bbox_inches='tight',
            facecolor='white'
        )
        plt.close(fig)
        
        logger.info(f"Visualizations saved to {output_path}")
        return True
        
    except Exception as e:
        logger.error(f"Visualization failed: {str(e)}", exc_info=True)
        return False