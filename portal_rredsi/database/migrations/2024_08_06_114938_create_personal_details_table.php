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
        Schema::create('personal_details', function (Blueprint $table) {
            $table->unsignedBigInteger('id_personal_detail')->primary()->autoIncrement();
            $table->unsignedBigInteger('id_document_type'); 
            $table->unsignedBigInteger('id_user'); 
            $table->string('document',55)->nullable(false); 
            $table->string('names',25);
            $table->string('last_names',25); 
            $table->string('cell_phone',12)->nullable(false); 
            $table->unsignedBigInteger('id_institution'); 

            $table->foreign('id_document_type')->references('id_document_type')->on('document_types')->onDelete('cascade');
            $table->foreign('id_user')->references('id_user')->on('users')->onDelete('cascade'); 
            $table->foreign('id_institution')->references('id_institution')->on('institutions')->onDelete('cascade');
        });
    }



    /**
     * Reverse the migrations.
     */
    public function down(): void
    {   
        Schema::dropIfExists('personal_details');
    }
};
