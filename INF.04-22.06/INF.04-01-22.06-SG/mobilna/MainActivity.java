package com.example.inf04_01_2206_sg_zadanie2;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
    int likes = 0;
    TextView likesCounter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        likesCounter = findViewById(R.id.likesCounter);
    }

    private void refreshLikesCounter() {
        likesCounter.setText(likes + " polubień");
    }

    public void onClickBtnLike(View view) {
        likes++;
        refreshLikesCounter();
    }

    public void onClickBtnDelete(View view) {
        likes--;
        if(likes < 0) {
            likes = 0;
        }
        refreshLikesCounter();
    }
}
