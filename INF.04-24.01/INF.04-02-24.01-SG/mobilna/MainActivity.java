package com.example.egzamin;

import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.SeekBar;
import android.widget.TextView;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class MainActivity extends AppCompatActivity {

    EditText etOwner, etGoal, etTime;
    TextView tvAge, tvStatus;
    SeekBar sbAge;
    ListView lvSpecies;
    Button btnOK;

    String[] species = {"pies", "kot", "świnka morska"};
    int selectedAnimal = 0;


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

        etOwner = findViewById(R.id.etOwner);
        etGoal = findViewById(R.id.etGoal);
        etTime = findViewById(R.id.etTime);
        tvAge = findViewById(R.id.tvAge);
        tvStatus = findViewById(R.id.tvStatus);
        sbAge = findViewById(R.id.sbAge);
        lvSpecies = findViewById(R.id.lvSpecies);
        btnOK = findViewById(R.id.btnOK);

        sbAge.setOnSeekBarChangeListener(new SeekBar.OnSeekBarChangeListener() {
            @Override
            public void onProgressChanged(SeekBar seekBar, int progress, boolean fromUser) {
                tvAge.setText(String.format("%d", progress));
            }

            @Override
            public void onStartTrackingTouch(SeekBar seekBar) {

            }

            @Override
            public void onStopTrackingTouch(SeekBar seekBar) {

            }
        });

        ArrayAdapter<String> arrayAdapter = new ArrayAdapter<>(this, android.R.layout.simple_list_item_1, species);
        lvSpecies.setAdapter(arrayAdapter);

        lvSpecies.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                selectedAnimal = position;
                String animal = (String) lvSpecies.getItemAtPosition(position);
                if (animal.equals("pies")) {
                    sbAge.setMax(18);
                } else if (animal.equals("kot")) {
                    sbAge.setMax(20);
                } else if (animal.equals("świnka morska")) {
                    sbAge.setMax(9);
                }
            }
        });

        btnOK.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                tvStatus.setText(String.format("%s, %s, %d, %s, %s",
                        etOwner.getText().toString(),
                        (String) lvSpecies.getItemAtPosition(selectedAnimal),
                        sbAge.getProgress(),
                        etGoal.getText().toString(),
                        etTime.getText().toString()));
            }
        });
    }
}