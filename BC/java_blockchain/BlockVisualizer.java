package java_blockchain;
import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.layout.Pane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Line;
import javafx.scene.text.Text;
import javafx.stage.Stage;

import java.util.List;

public class BlockVisualizer extends Application {

    private Blockchain blockchain;
    
    public BlockVisualizer(Blockchain blockchain) {
        this.blockchain = blockchain;
    }

    @Override
    public void start(Stage primaryStage) {
        Pane pane = new Pane();
        
        List<Block> blocks = blockchain.getChain();
        
        // Visualize each block
        double yPosition = 50;
        double blockWidth = 200;
        double blockHeight = 100;
        
        for (int i = 0; i < blocks.size(); i++) {
            Block block = blocks.get(i);
            
            // Create a block (represented as a rectangle with text)
            javafx.scene.shape.Rectangle blockRect = new javafx.scene.shape.Rectangle(blockWidth, blockHeight);
            blockRect.setFill(Color.LIGHTBLUE);
            blockRect.setStroke(Color.BLACK);
            
            // Set the position of the block
            blockRect.setX(100);
            blockRect.setY(yPosition);
            
            // Add the block's hash as text
            Text text = new Text(block.getHash());
            text.setX(110);
            text.setY(yPosition + 20);
            
            // If not the first block, draw a line connecting it to the previous block
            if (i > 0) {
                Block previousBlock = blocks.get(i - 1);
                Line line = new Line(
                        100 + blockWidth / 2, yPosition, 
                        100 + blockWidth / 2, yPosition - 50);
                line.setStroke(Color.BLACK);
                pane.getChildren().add(line);
            }

            // Add the rectangle and text to the pane
            pane.getChildren().addAll(blockRect, text);
            
            // Move the position for the next block
            yPosition += blockHeight + 20;
        }
        
        Scene scene = new Scene(pane, 600, 600);
        primaryStage.setTitle("Blockchain Visualization");
        primaryStage.setScene(scene);
        primaryStage.show();
    }
    
    public static void visualizeBlockchain(Blockchain blockchain) {
        BlockVisualizer visualizer = new BlockVisualizer(blockchain);
        launch();
    }
}
