package com.example.inf04_02_2301_sg_zadanie2;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.EditText;
import android.widget.ListView;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {
    private ArrayList<String> noteList;
    ArrayAdapter<String> arrayAdapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        noteList = new ArrayList<>();
        noteList.add("Zakupy: chleb, masło, ser");
        noteList.add("Do zrobienia: obiad, umyć podłogi");
        noteList.add("weekend: kino, spacer z psem");

        arrayAdapter = new ArrayAdapter<>(this, android.R.layout.simple_list_item_1, noteList);

        ListView listView = (ListView) findViewById(R.id.listView);
        listView.setAdapter(arrayAdapter);
    }
    
    public void onClick(View view) {
        EditText editText = (EditText) findViewById(R.id.newElement);
        String note = editText.getText().toString();

        noteList.add(note);
        arrayAdapter.notifyDataSetChanged();
    }
}
