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
        Schema::create('phases', function (Blueprint $table) {
            $table->unsignedBigInteger('id_phase')->primary()->autoIncrement();
            $table->string('names',30)->nullable(false);
            $table->unsignedBigInteger('id_stage'); 
            $table->foreign('id_stage')->references('id_stage')->on('stages')->onDelete('cascade');
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('phases');
    }
};
