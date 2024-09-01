<template>
    <tbody>
        <tr v-for="(item, index) in rubricaItems" :key="index" class=" w-100">
            <td class="border border-dark">{{ item.componente }}</td>
            <td class="border border-dark">{{ item.maxValor }}</td>
            <td class="border border-dark">
                <input 
                    type="number" 
                    class="form-control fs-6 form-control-sm" 
                    v-model="item.calificacion" 
                    readonly
                >
            </td>
            <td class="border border-dark">
                <textarea 
                    class="form-control fs-6 form-control-sm" 
                    v-model="item.observaciones" 
                    readonly
                ></textarea>
            </td>
        </tr>
    </tbody>
</template>

<script>
export default {
    name: 'RubricaBody',
    props: {
        rubricaItems: {
            type: Array,
            required: true
        }
    }
}
</script>

<style scoped>
.text-center {
    text-align: center;
}

td {
    vertical-align: middle;
}

input[type="number"].form-control,
textarea.form-control {
    display: block;
    margin: auto;
    text-align: center;
}
</style>

