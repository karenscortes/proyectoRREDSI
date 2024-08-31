<template>
        <select type="select" class="form-select text-dark">
            <option :value="defaultOption " selected>{{ defaultOption  }}</option>
            <option v-for="opcion in opciones" :value="opcion" :key="opcion">
                {{ opcion }}
            </option>
        </select>
</template>
<script>
export default{
    name:"ComponenteSelect",
    props:{
        defaultOption: String,
        opciones: Array
    }
}
</script>