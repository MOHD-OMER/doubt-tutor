"""
Custom exceptions for Doubt Tutor
"""


class DoubtTutorError(Exception):
    """Base exception for Doubt Tutor application"""
    pass


class FileProcessingError(DoubtTutorError):
    """Exception raised when file processing fails"""
    pass


class OCRError(DoubtTutorError):
    """Exception raised when OCR fails"""
    pass


class AIModelError(DoubtTutorError):
    """Exception raised when AI model interaction fails"""
    pass


class DatabaseError(DoubtTutorError):
    """Exception raised for database operations"""
    pass


class ValidationError(DoubtTutorError):
    """Exception raised for validation failures"""
    pass
