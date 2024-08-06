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
        Schema::create('area_conocimientos', function (Blueprint $table) {
            $table->unsignedBigInteger('id_area_conocimiento')->primary()->autoIncrement();
            $table->string('nombre',35);
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('area_conocimientos');
    }
};
