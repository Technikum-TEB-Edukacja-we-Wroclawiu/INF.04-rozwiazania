package com.example.inf04_informator;

import androidx.appcompat.app.AppCompatActivity;

import android.graphics.Color;
import android.os.Bundle;
import android.text.Editable;
import android.text.TextWatcher;
import android.view.View;
import android.widget.CompoundButton;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.Switch;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {
    private final int[] images = {
            R.drawable.kot1,
            R.drawable.kot2,
            R.drawable.kot3,
            R.drawable.kot4
    };
    ImageView iv; // Dostęp do ImageView z obrazkiem kota
    EditText etImageNumber; // Dostęp do EditText z numerem obrazka
    Switch switchBackground; // Dostęp do Switcha
    LinearLayout layout; // Dostęp do layoutu aplikacji (żeby potem zmienić tło)
    int current_image = 0; // Indeks bieżącego obrazka - standardowo od 0

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        iv = findViewById(R.id.imageView);
        etImageNumber = findViewById(R.id.editTextNumber);
        switchBackground = findViewById(R.id.switchBackground);
        layout = findViewById(R.id.layout);

        etImageNumber.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence charSequence, int i, int i1, int i2) {

            }

            @Override
            public void onTextChanged(CharSequence charSequence, int i, int i1, int i2) {

            }

            @Override
            public void afterTextChanged(Editable editable) {
                String imageNumberInput = editable.toString();
                int imageNumber;
                try {
                    imageNumber = Integer.parseInt(imageNumberInput);
                } catch(NumberFormatException ex) {
                    return;
                }

                if(imageNumber >= 1 && imageNumber <= images.length) {
                    current_image = imageNumber - 1;
                    iv.setImageResource(images[current_image]);
                }
            }
        });

        switchBackground.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton compoundButton, boolean b) {
                if(b) {
                    // ustaw tło na niebieski
                    layout.setBackgroundColor(Color.parseColor("#1565c0"));
                } else {
                    // ustaw tło na standardowe
                    layout.setBackgroundColor(Color.parseColor("#00796B"));
                }
            }
        });
    }

    public void onClickBtnNext(View view) {
        current_image = (current_image + 1) % images.length;
        iv.setImageResource(images[current_image]);

        // I sposób wprowadzenia liczby do pola tekstowego
        // - ustalenie wartości i konwersja jej przez Integer.toString()
        int image_number = current_image + 1;
        etImageNumber.setText(Integer.toString(image_number));
    }

    public void onClickBtnPrev(View view) {
        // 0 - 1 = -1
        // (-1) mod 4 = 3
        // niestety operator% w Javie nie działa tak jak w Pythonie
        current_image = current_image - 1;
        if(current_image < 0) {
            current_image += images.length; // np. -1 + 4 = 3
        }
        iv.setImageResource(images[current_image]);

        // II sposób wprowadzenia - String.format()
        etImageNumber.setText(String.format("%d", current_image + 1));
    }
}






