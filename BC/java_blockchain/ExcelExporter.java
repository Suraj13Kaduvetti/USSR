package java_blockchain;
import org.apache.poi.ss.usermodel.*;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

import java.io.FileOutputStream;
import java.io.IOException;
import java.util.List;

public class ExcelExporter {
    public static void exportLedgerToExcel(List<String> ledgerEntries) {
        Workbook workbook = new XSSFWorkbook();
        Sheet sheet = workbook.createSheet("Ledger");
        Row header = sheet.createRow(0);
        header.createCell(0).setCellValue("Timestamp");
        header.createCell(1).setCellValue("Data Type");
        
        int rowNum = 1;
        for (String entry : ledgerEntries) {
            Row row = sheet.createRow(rowNum++);
            String[] parts = entry.split(" | ");
            row.createCell(0).setCellValue(parts[0].split(":")[1].trim());
            row.createCell(1).setCellValue(parts[1].split(":")[1].trim());
        }

        try (FileOutputStream fileOut = new FileOutputStream("ledger.xlsx")) {
            workbook.write(fileOut);
            workbook.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
