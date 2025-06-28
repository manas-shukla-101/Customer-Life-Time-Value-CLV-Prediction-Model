import time
import sys
from utils.logger import get_logger

logger = get_logger(__name__)

class ProgressTracker:
    def __init__(self, total_steps: int = 10):
        self.total_steps = total_steps
        self.current_step = 0
        self.start_time = time.time()
        
    def update(self, message: str):
        """Update progress with message."""
        self.current_step += 1
        progress = self.current_step / self.total_steps
        bar = '█' * int(40 * progress) + '-' * (40 - int(40 * progress))
        
        sys.stdout.write(f'\r[{bar}] {progress:.0%} - {message}')
        sys.stdout.flush()
        
        if self.current_step == self.total_steps:
            elapsed = time.time() - self.start_time
            print(f'\nCompleted in {elapsed:.2f} seconds')
            logger.info(f"Completed all steps in {elapsed:.2f} seconds")