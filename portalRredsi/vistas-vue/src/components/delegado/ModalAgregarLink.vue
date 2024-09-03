<template>
    <div v-if="isVisible" class="modal fade show d-block" tabindex="-1" @click.self="closeModal">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content border border-dark border-3 rounded-3 text-dark">
                <span class="close" @click="closeModal">&times;</span>
                <h4 class="text-center">Agregar presentación</h4>
                <form @submit.prevent="handleSubmit">
                    <div class="form-group mb-4">
                        <label for="linkPresentacion">Link:</label>
                        <input type="text" v-model="link" class="form-control form-control-lg" id="linkPresentacion"
                            style="font-size: 1rem;" />
                    </div>
                    <div class="text-center">
                        <button type="submit" class="btn btn-dark font-weight-bold w-100"
                            style="font-size: 1rem; padding: 0.5rem;">
                            Añadir
                        </button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        isVisible: Boolean,
    },
    data() {
        return {
            link: '', 
        };
    },
    methods: {
        closeModal() {
            this.$emit('close');
        },
        handleSubmit() {
            this.saveLink(this.link);
            this.closeModal();
        },
        saveLink(link) {
            console.log('Guardado con éxito:', link);
        },
    },
};
</script>

<style scoped>
.modal {
    display: block;
    position: fixed;
    z-index: 1;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    overflow: auto;
    background-color: rgba(0, 0, 0, 0.4);
}

.modal-content {
    background-color: #fefefe;
    margin: 10% auto;
    padding: 20px;
    border: 1px solid #888;
    width: 90%;
    max-width: 500px;
    border-radius: 8px;
    position: relative;
}

.close {
    color: #aaa;
    font-size: 24px;
    font-weight: bold;
    cursor: pointer;
    position: absolute;
    top: 10px;
    right: 10px;
}

.close:hover,
.close:focus {
    color: black;
    text-decoration: none;
}

.form-group {
    margin-bottom: 20px;
}

.form-control {
    width: 100%;
    padding: 12px;
    box-sizing: border-box;
    border-radius: 4px;
    border: 1px solid #ccc;
}

.btn {
    padding: 10px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

.w-100 {
    width: 100% !important;
}
</style>
