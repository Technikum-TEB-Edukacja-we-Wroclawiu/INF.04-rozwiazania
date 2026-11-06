package com.example.kostki;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

import java.util.LinkedList;

public class MainActivity extends AppCompatActivity {
    Button rollDice,resetGame;;

    TextView rollScore,gameScore;;
    int total_score=0;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_main);
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;
        });
        rollDice=findViewById(R.id.rollDiceButton);
        resetGame=findViewById(R.id.resetGameButton);

        rollScore=findViewById(R.id.rollScoreTextView);
        gameScore=findViewById(R.id.gameScoreTextView);


        rollDice.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                int score=diceGame();
                total_score+=score;
                rollScore.setText("Wynik tego losowania:"+score);
                gameScore.setText("Wynik gry:"+total_score);

            }
        });
        resetGame.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                total_score=0;
                changeImages(new int[]{0,0,0,0,0});
                rollScore.setText("Wynik tego losowania:0");
                gameScore.setText("Wynik gry:"+total_score);

            }
        });
    }
    public  int diceGame(){
        int dice_array[]=new int[5];
        int score=0;
        for(int i=0;i<5;i++){
            dice_array[i]=(int)(Math.random()*6)+1;
        }

        changeImages(dice_array);
        LinkedList<Integer>checked_numbers=new LinkedList<>();
        for(int i=0;i<5;i++){
            if(!checked_numbers.contains(dice_array[i])){
                checked_numbers.add(dice_array[i]);
                int occurrences_number=1;
                for(int j=i+1;j<5;j++){
                    if(dice_array[i]==dice_array[j]){
                        occurrences_number++;
                    }
                }
                if(occurrences_number>=2){
                    score+=dice_array[i]*occurrences_number;
                }
            }
        }

        return score;
    }
    public  void changeImages(int dice_array[]){
        int[]images={R.id.firstDiceImageView,R.id.anotherDiceImageView,R.id.thirdDiceImageView,R.id.fourthDiceImageView,R.id.fifthDiceImageView};
        int[]drawable_images={R.drawable.question,R.drawable.k1,R.drawable.k2,R.drawable.k3,R.drawable.k4,R.drawable.k5,R.drawable.k6};
        for(int i=0;i<5;i++){
            int image_id=0;
            ImageView imageView=findViewById(images[i]);
            image_id=drawable_images[dice_array[i]];
            imageView.setImageResource(image_id);

        }
    }
}