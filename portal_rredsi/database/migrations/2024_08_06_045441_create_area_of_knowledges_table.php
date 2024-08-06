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
        Schema::create('area_of_knowledges', function (Blueprint $table) {
            $table->unsignedBigInteger('id_area_of_knowledge')->primary()->autoIncrement();
            $table->string('names',35)->nullable(false);
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('area_of_knowledges');
    }
};
