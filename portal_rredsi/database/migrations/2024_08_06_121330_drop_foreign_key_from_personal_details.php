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
        Schema::table('personal_details', function (Blueprint $table) {
            //
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::table('personal_details', function (Blueprint $table) {
            $table->dropForeign(['id_document_type']); 
            $table->dropColumn('id_document_type'); 
            $table->dropForeign(['id_user']); 
            $table->dropColumn('id_user'); 
        });
    }
};
