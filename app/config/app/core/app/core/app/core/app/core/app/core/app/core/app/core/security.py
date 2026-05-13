from app.core.logger import logger


class SafetyManager:
    @staticmethod
    def validate_limits(current, maximum):
        if current >= maximum:
            logger.warning("Daily action limit reached")
            return False
        return True
