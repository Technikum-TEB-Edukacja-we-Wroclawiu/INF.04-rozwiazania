package com.example.urzdom

import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import org.w3c.dom.Text

class MainActivity : AppCompatActivity() {
    private lateinit var etWashingProgram: EditText
    private lateinit var tvWashingProgram: TextView
    private lateinit var tvVacuumOnOff: TextView
    private lateinit var tvVacuumStatus: TextView
    private lateinit var btnVacuumOnOff: Button

    private var vacuumStatus = false

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_main)
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main)) { v, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom)
            insets
        }

        etWashingProgram = findViewById(R.id.etWashingProgram)
        tvWashingProgram = findViewById(R.id.tvWashingProgram)
        tvVacuumOnOff = findViewById(R.id.tvVacuumOnOff)
        tvVacuumStatus = findViewById(R.id.tvVacuumStatus)
        btnVacuumOnOff = findViewById(R.id.btnVacuumOnOff)
    }

    fun setWashingProgram(view: View) {
        val program: Int = Integer.parseInt(etWashingProgram.text.toString())
        if (program in 1..12) {
            tvWashingProgram.text = "Numer prania: $program"
        }
    }

    fun vacuumOnOff(view: View) {
        if(!vacuumStatus) {
            vacuumStatus = true
            btnVacuumOnOff.text = "Wyłącz"
            tvVacuumOnOff.text = "Odkurzacz włączony"
        } else {
            vacuumStatus = false
            btnVacuumOnOff.text = "Włącz"
            tvVacuumOnOff.text = "Odkurzacz wyłączony"
        }
    }
}