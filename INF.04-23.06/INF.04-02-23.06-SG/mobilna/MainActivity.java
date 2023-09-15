package com.example.inf04_02_2306_sg_zadanie2;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.QuickContactBadge;
import android.widget.SeekBar;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
    TextView text_size, text_quote;
    SeekBar seekBar;
    Button button_next;

    String[] quotes = {
            "Dzień dobry",
            "Good morning",
            "Buenos dias"
    };
    int current_quote = 0;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        text_size = findViewById(R.id.text_size);
        text_quote = findViewById(R.id.text_quote);
        seekBar = findViewById(R.id.seekBar);
        button_next = findViewById(R.id.button_next);

        text_quote.setText(quotes[current_quote]);

        seekBar.setOnSeekBarChangeListener(new SeekBar.OnSeekBarChangeListener() {
            @Override
            public void onProgressChanged(SeekBar seekBar, int i, boolean b) {
                text_size.setText("Rozmiar: " + Integer.toString(i));
                text_quote.setTextSize((float)i);
            }

            @Override
            public void onStartTrackingTouch(SeekBar seekBar) {}

            @Override
            public void onStopTrackingTouch(SeekBar seekBar) {}
        });

        button_next.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                current_quote += 1;
                if(current_quote == quotes.length) {
                    current_quote = 0;
                }

                text_quote.setText(quotes[current_quote]);
            }
        });
    }
}