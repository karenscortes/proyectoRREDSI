<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('phase_programmings', function (Blueprint $table) {
            $table->unsignedBigInteger('id_phase_programming')->primary()->autoIncrement();
            $table->unsignedBigInteger('id_phase');
            $table->unsignedBigInteger('id_announcement'); 
            $table->date('start_dates');
            $table->date('end_dates');

            $table->foreign('id_phase')->references('id_phase')->on('phases')->onDelete('cascade');
            $table->foreign('id_announcement')->references('id_announcement')->on('announcements')->onDelete('cascade');
        });
    }


    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('phase_programmings');
    }
};
