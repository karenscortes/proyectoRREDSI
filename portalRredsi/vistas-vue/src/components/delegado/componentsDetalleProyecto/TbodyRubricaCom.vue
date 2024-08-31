<template>
    <tr v-for="(componente, index) in componentes" :key="index">
        <td class="border border-dark">
            <span class="text-dark font-weight-bold">Titulo:</span> {{ componente.titulo }}
        </td>
        <td class="text-center border border-dark">{{ componente.valorMaximo }}</td>
        <td class="border border-dark">
            <input type="number" v-model.number="componente.calificacion" class="w-100">
        </td>
        <td class="border border-dark">
            <textarea v-model="componente.observaciones" class="w-100" rows="1"></textarea>
        </td>
    </tr>
</template>