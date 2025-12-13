"""
Modern UI for PDF Text Extractor
Beautiful and attractive interface with enhanced user experience
"""

from PyQt5.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QTextEdit,
    QLabel,
    QFileDialog,
    QProgressBar,
    QStatusBar,
    QMessageBox,
    QFrame,
    QGroupBox,
)
from PyQt5.QtCore import Qt, QThread, pyqtSignal


class ExtractionThread(QThread):
    """Thread for PDF extraction to prevent UI freezing"""
    finished = pyqtSignal(str, bool, str)  # text, success, error_message
    progress = pyqtSignal(int, str)  # progress_percentage, status_message

    def __init__(self, pdf_path, extractor_function):
        super().__init__()
        self.pdf_path = pdf_path
        self.extractor_function = extractor_function

    def run(self):
        try:
            self.progress.emit(10, "Reading PDF file...")
            text = self.extractor_function(self.pdf_path, self.progress)
            self.progress.emit(100, "Extraction complete!")
            self.finished.emit(text, True, "")
        except Exception as e:
            self.finished.emit("", False, str(e))


class PDFExtractorUI(QMainWindow):
    """Modern, attractive UI for PDF Text Extractor"""

    def __init__(self, extractor_function):
        super().__init__()
        self.extractor_function = extractor_function
        self.pdf_path = None
        self.extraction_thread = None
        self.initUI()

    def initUI(self):
        """Initialize the user interface"""
        self.setGeometry(100, 100, 1200, 800)
        self.setWindowTitle("PDF Text Extractor - Professional Edition")
        
        # Apply modern styling
        self.applyModernStyle()
        
        # Create central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(20, 20, 20, 20)

        # Header section
        self.createHeader(main_layout)

        # File selection section
        self.createFileSection(main_layout)

        # Control buttons section
        self.createControlSection(main_layout)

        # Text display section
        self.createTextDisplaySection(main_layout)

        # Progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                border: 2px solid #3498db;
                border-radius: 8px;
                text-align: center;
                height: 25px;
                background-color: #ecf0f1;
            }
            QProgressBar::chunk {
                background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #3498db, stop:1 #2980b9);
                border-radius: 6px;
            }
        """)
        main_layout.addWidget(self.progress_bar)

        # Status bar
        self.status_bar = QStatusBar()
        self.status_bar.setStyleSheet("""
            QStatusBar {
                background-color: #34495e;
                color: white;
                border-top: 2px solid #2c3e50;
                padding: 5px;
            }
        """)
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("Ready - Select a PDF file to begin")

    def createHeader(self, parent_layout):
        """Create attractive header section"""
        header_frame = QFrame()
        header_frame.setStyleSheet("""
            QFrame {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #3498db, stop:1 #2980b9);
                border-radius: 10px;
                padding: 20px;
            }
        """)
        header_layout = QVBoxLayout(header_frame)
        header_layout.setContentsMargins(20, 15, 20, 15)

        title_label = QLabel("📄 PDF Text Extractor")
        title_label.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 32px;
                font-weight: bold;
                background: transparent;
                border: none;
            }
        """)
        title_label.setAlignment(Qt.AlignCenter)

        subtitle_label = QLabel("Extract text from PDF files with high accuracy")
        subtitle_label.setStyleSheet("""
            QLabel {
                color: #ecf0f1;
                font-size: 14px;
                background: transparent;
                border: none;
            }
        """)
        subtitle_label.setAlignment(Qt.AlignCenter)

        header_layout.addWidget(title_label)
        header_layout.addWidget(subtitle_label)
        parent_layout.addWidget(header_frame)

    def createFileSection(self, parent_layout):
        """Create file selection section"""
        file_group = QGroupBox("📁 File Selection")
        file_group.setStyleSheet("""
            QGroupBox {
                font-size: 16px;
                font-weight: bold;
                color: #2c3e50;
                border: 2px solid #bdc3c7;
                border-radius: 8px;
                margin-top: 10px;
                padding-top: 15px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
            }
        """)
        file_layout = QHBoxLayout(file_group)
        file_layout.setSpacing(10)

        self.file_label = QLabel("No file selected")
        self.file_label.setStyleSheet("""
            QLabel {
                padding: 10px;
                background-color: #ecf0f1;
                border: 2px dashed #bdc3c7;
                border-radius: 5px;
                color: #7f8c8d;
                font-size: 13px;
            }
        """)
        self.file_label.setWordWrap(True)

        self.btn_browse = QPushButton("Browse...")
        self.btn_browse.setStyleSheet(self.getButtonStyle("#3498db", "#2980b9"))
        self.btn_browse.setFixedWidth(120)
        self.btn_browse.clicked.connect(self.openPDF)

        file_layout.addWidget(self.file_label, 1)
        file_layout.addWidget(self.btn_browse)
        parent_layout.addWidget(file_group)

    def createControlSection(self, parent_layout):
        """Create control buttons section"""
        control_layout = QHBoxLayout()
        control_layout.setSpacing(15)

        self.btn_extract = QPushButton("🚀 Extract Text")
        self.btn_extract.setStyleSheet(self.getButtonStyle("#27ae60", "#229954", hover="#2ecc71"))
        self.btn_extract.setMinimumHeight(45)
        self.btn_extract.clicked.connect(self.extractText)
        self.btn_extract.setEnabled(False)

        self.btn_clear = QPushButton("🗑️ Clear")
        self.btn_clear.setStyleSheet(self.getButtonStyle("#e74c3c", "#c0392b", hover="#ec7063"))
        self.btn_clear.setMinimumHeight(45)
        self.btn_clear.clicked.connect(self.clearText)

        self.btn_save = QPushButton("💾 Save Text")
        self.btn_save.setStyleSheet(self.getButtonStyle("#f39c12", "#e67e22", hover="#f4a460"))
        self.btn_save.setMinimumHeight(45)
        self.btn_save.clicked.connect(self.saveText)

        control_layout.addWidget(self.btn_extract)
        control_layout.addWidget(self.btn_clear)
        control_layout.addWidget(self.btn_save)
        parent_layout.addLayout(control_layout)

    def createTextDisplaySection(self, parent_layout):
        """Create text display section"""
        text_group = QGroupBox("📝 Extracted Text")
        text_group.setStyleSheet("""
            QGroupBox {
                font-size: 16px;
                font-weight: bold;
                color: #2c3e50;
                border: 2px solid #bdc3c7;
                border-radius: 8px;
                margin-top: 10px;
                padding-top: 15px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
            }
        """)
        text_layout = QVBoxLayout(text_group)

        # Character count label
        self.char_count_label = QLabel("Characters: 0 | Words: 0")
        self.char_count_label.setStyleSheet("""
            QLabel {
                color: #7f8c8d;
                font-size: 12px;
                padding: 5px;
                background-color: #ecf0f1;
                border-radius: 4px;
            }
        """)

        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        self.text_edit.setStyleSheet("""
            QTextEdit {
                background-color: #ffffff;
                border: 2px solid #bdc3c7;
                border-radius: 8px;
                padding: 10px;
                font-family: 'Segoe UI', Arial, sans-serif;
                font-size: 12px;
                color: #2c3e50;
                selection-background-color: #3498db;
            }
            QTextEdit:focus {
                border: 2px solid #3498db;
            }
        """)
        self.text_edit.textChanged.connect(self.updateCharCount)

        text_layout.addWidget(self.char_count_label)
        text_layout.addWidget(self.text_edit)
        parent_layout.addWidget(text_group, 1)  # Stretch factor

    def getButtonStyle(self, color1, color2, hover=None):
        """Get styled button CSS"""
        hover_color = hover if hover else color1
        return f"""
            QPushButton {{
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 {color1}, stop:1 {color2});
                color: white;
                border: none;
                border-radius: 8px;
                padding: 10px 20px;
                font-size: 14px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 {hover_color}, stop:1 {color2});
            }}
            QPushButton:pressed {{
                background-color: {color2};
            }}
            QPushButton:disabled {{
                background-color: #95a5a6;
                color: #7f8c8d;
            }}
        """

    def applyModernStyle(self):
        """Apply modern styling to the application"""
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f8f9fa;
            }
            QPushButton {
                min-height: 35px;
            }
        """)

    def openPDF(self):
        """Open PDF file dialog"""
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        pdf_file, _ = QFileDialog.getOpenFileName(
            self,
            "Open PDF File",
            "",
            "PDF Files (*.pdf);;All Files (*)",
            options=options,
        )
        if pdf_file:
            self.pdf_path = pdf_file
            file_name = pdf_file.split("/")[-1] if "/" in pdf_file else pdf_file.split("\\")[-1]
            self.file_label.setText(f"Selected: {file_name}")
            self.file_label.setStyleSheet("""
                QLabel {
                    padding: 10px;
                    background-color: #d5f4e6;
                    border: 2px solid #27ae60;
                    border-radius: 5px;
                    color: #229954;
                    font-size: 13px;
                    font-weight: bold;
                }
            """)
            self.btn_extract.setEnabled(True)
            self.status_bar.showMessage(f"File loaded: {file_name}")

    def extractText(self):
        """Extract text from PDF"""
        if not self.pdf_path:
            QMessageBox.warning(self, "No File", "Please select a PDF file first.")
            return

        # Disable buttons during extraction
        self.btn_extract.setEnabled(False)
        self.btn_browse.setEnabled(False)
        self.progress_bar.setVisible(True)
        self.progress_bar.setValue(0)
        self.text_edit.clear()
        self.status_bar.showMessage("Extracting text... Please wait.")

        # Create and start extraction thread
        self.extraction_thread = ExtractionThread(self.pdf_path, self.extractor_function)
        self.extraction_thread.progress.connect(self.updateProgress)
        self.extraction_thread.finished.connect(self.onExtractionFinished)
        self.extraction_thread.start()

    def updateProgress(self, value, message):
        """Update progress bar and status"""
        self.progress_bar.setValue(value)
        self.status_bar.showMessage(message)

    def onExtractionFinished(self, text, success, error_message):
        """Handle extraction completion"""
        self.progress_bar.setVisible(False)
        self.btn_extract.setEnabled(True)
        self.btn_browse.setEnabled(True)

        if success:
            self.text_edit.setPlainText(text)
            char_count = len(text)
            word_count = len(text.split()) if text else 0
            self.status_bar.showMessage(
                f"Extraction complete! {char_count} characters, {word_count} words extracted."
            )
            if not text.strip():
                QMessageBox.warning(
                    self,
                    "Empty Result",
                    "No text could be extracted from this PDF. It might be a scanned document or image-based PDF."
                )
        else:
            QMessageBox.critical(
                self,
                "Extraction Error",
                f"An error occurred during extraction:\n\n{error_message}"
            )
            self.status_bar.showMessage("Extraction failed. Please try again.")

    def clearText(self):
        """Clear extracted text"""
        self.text_edit.clear()
        self.status_bar.showMessage("Text cleared")

    def saveText(self):
        """Save extracted text to file"""
        text = self.text_edit.toPlainText()
        if not text:
            QMessageBox.warning(self, "No Text", "No text to save. Please extract text first.")
            return

        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save Text File",
            "",
            "Text Files (*.txt);;All Files (*)",
            options=options,
        )
        if file_path:
            try:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(text)
                QMessageBox.information(self, "Success", "Text saved successfully!")
                self.status_bar.showMessage(f"Text saved to: {file_path}")
            except Exception as e:
                QMessageBox.critical(self, "Save Error", f"Could not save file:\n\n{str(e)}")

    def updateCharCount(self):
        """Update character and word count"""
        text = self.text_edit.toPlainText()
        char_count = len(text)
        word_count = len(text.split()) if text else 0
        self.char_count_label.setText(f"Characters: {char_count:,} | Words: {word_count:,}")
        
        
        



"""
PDF Text Extractor - Main Application
Uses pdfplumber for accurate text extraction with improved logic
"""

import sys
import os

try:
    import pdfplumber
    PDFPLUMBER_AVAILABLE = True
except ImportError:
    PDFPLUMBER_AVAILABLE = False
    print("Warning: pdfplumber not found. Falling back to PyPDF2.")
    try:
        from PyPDF2 import PdfReader
        PYPDF2_AVAILABLE = True
    except ImportError:
        PYPDF2_AVAILABLE = False
        print("Error: Neither pdfplumber nor PyPDF2 is installed.")
        sys.exit(1)

from PyQt5.QtWidgets import QApplication
from pdf_extractor_ui import PDFExtractorUI


def extract_text_with_pdfplumber(pdf_path, progress_callback=None):
    """
    Extract text from PDF using pdfplumber (more accurate)
    
    Args:
        pdf_path: Path to the PDF file
        progress_callback: Optional callback function(percentage, message)
    
    Returns:
        Extracted text as string
    """
    pdf_text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            total_pages = len(pdf.pages)
            
            for page_num, page in enumerate(pdf.pages, 1):
                if progress_callback:
                    progress = 10 + int((page_num / total_pages) * 80)
                    progress_callback(progress, f"Extracting page {page_num} of {total_pages}...")
                
                # Extract text with layout preservation
                page_text = page.extract_text()
                
                if page_text:
                    # Add page separator for better readability
                    if pdf_text:
                        pdf_text += f"\n\n{'='*80}\n"
                        pdf_text += f"PAGE {page_num}\n"
                        pdf_text += f"{'='*80}\n\n"
                    else:
                        pdf_text += f"PAGE {page_num}\n"
                        pdf_text += f"{'='*80}\n\n"
                    
                    pdf_text += page_text
                    
                    # Try to extract tables if present (optional enhancement)
                    tables = page.extract_tables()
                    if tables:
                        for table in tables:
                            pdf_text += "\n\n[Table Found]\n"
                            for row in table:
                                if row:
                                    pdf_text += " | ".join(str(cell) if cell else "" for cell in row)
                                    pdf_text += "\n"
                
        return pdf_text.strip()
    
    except Exception as e:
        raise Exception(f"Error extracting text with pdfplumber: {str(e)}")


def extract_text_with_pypdf2(pdf_path, progress_callback=None):
    """
    Extract text from PDF using PyPDF2 (fallback method)
    
    Args:
        pdf_path: Path to the PDF file
        progress_callback: Optional callback function(percentage, message)
    
    Returns:
        Extracted text as string
    """
    pdf_text = ""
    try:
        pdf_reader = PdfReader(pdf_path)
        total_pages = len(pdf_reader.pages)
        
        for page_num, page in enumerate(pdf_reader.pages, 1):
            if progress_callback:
                progress = 10 + int((page_num / total_pages) * 80)
                progress_callback(progress, f"Extracting page {page_num} of {total_pages}...")
            
            try:
                page_text = page.extract_text()
                if page_text:
                    if pdf_text:
                        pdf_text += f"\n\n{'='*80}\n"
                        pdf_text += f"PAGE {page_num}\n"
                        pdf_text += f"{'='*80}\n\n"
                    else:
                        pdf_text += f"PAGE {page_num}\n"
                        pdf_text += f"{'='*80}\n\n"
                    pdf_text += page_text
            except Exception as e:
                # Continue with next page if one page fails
                pdf_text += f"\n\n[Error extracting page {page_num}: {str(e)}]\n\n"
                continue
        
        return pdf_text.strip()
    
    except Exception as e:
        raise Exception(f"Error extracting text with PyPDF2: {str(e)}")


def extract_text_from_pdf(pdf_path, progress_callback=None):
    """
    Main extraction function that tries the best available method
    
    Args:
        pdf_path: Path to the PDF file
        progress_callback: Optional callback function(percentage, message)
    
    Returns:
        Extracted text as string
    """
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")
    
    if PDFPLUMBER_AVAILABLE:
        return extract_text_with_pdfplumber(pdf_path, progress_callback)
    elif PYPDF2_AVAILABLE:
        return extract_text_with_pypdf2(pdf_path, progress_callback)
    else:
        raise ImportError("No PDF extraction library available. Please install pdfplumber or PyPDF2.")


def main():
    """Main application entry point"""
    app = QApplication(sys.argv)
    
    # Set application properties
    app.setApplicationName("PDF Text Extractor")
    app.setOrganizationName("Fun Code")
    
    # Create and show the UI
    window = PDFExtractorUI(extract_text_from_pdf)
    window.show()
    
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()