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
        Schema::create('permissions', function (Blueprint $table) {
            $table->unsignedBigInteger('id_module'); 
            $table->unsignedBigInteger('id_role'); 
            $table->tinyInteger('p_insert')->default(false);
            $table->tinyInteger('p_select')->default(false);
            $table->tinyInteger('p_update')->default(false);
            $table->tinyInteger('p_delete')->default(false);
            $table->primary(['id_module','id_role']); 
            $table->foreign('id_module')->references('id_module')->on('modules')->onDelete('cascade');
            $table->foreign('id_role')->references('id_role')->on('roles')->onDelete('cascade');
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('permissions');
    }
};
