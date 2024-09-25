<template>
    <div class="feature">
        <div class="icon">
            <i class="fa-solid fa-user-group fa-lg text-dark mb-3"></i>
        </div>
        <h3 class="text-dark text-left">Suplentes <i type="button" class="fa-regular fa-square-plus fa-lg text-dark" @click="openModal"></i></h3>
        <p class="text-dark text-left">
            Tipo: {{ tipo }} <br> 
            Nombre: {{ suplente }}
        </p>
        <div v-if="isModalOpen" class="modal">
            <div class="modal-content">
                <span class="close" @click="closeModal">&times;</span>
                <h4>Agregar Suplente</h4>
                <div class="form-group">
                    <label for="tipo">Tipo:</label>
                    <select v-model="nuevoTipo" id="tipo" class="form-control">
                        <option value="" disabled selected>Seleccionar Tipo</option>
                        <option value="Ponente">Ponente</option>
                        <option value="Evaluador">Evaluador</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="nombre">Nombre:</label>
                    <input type="text" v-model="nuevoNombre" id="nombre" class="form-control" />
                </div>
                <button type="submit" class="btn btn-warning font-weight-bold" @click="addSuplente">Añadir</button>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'SuplentesCom',
    props: {
        tipo: {
            type: String,
            required: true,
        },
        suplente: {
            type: String,
            required: true,
        },
    },
    data() {
        return {
            isModalOpen: false, 
            nuevoTipo: '',        
            nuevoNombre: '',     
        };
    },
    methods: {
        openModal() {
            this.isModalOpen = true;
        },
        closeModal() {
            this.isModalOpen = false;
        },
        addSuplente() {
            this.nuevoTipo; 
            this.nuevoNombre;    
            this.nuevoTipo = '';
            this.nuevoNombre = '';
            this.closeModal();
        },
    },
};
</script>

<style scoped>
h3,
p {
    font-size: 0.9rem;
    margin-bottom: 5px;
}

.text-left {
    text-align: left;
}

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
    margin: 15% auto;
    padding: 20px;
    border: 1px solid #888;
    width: 400px;
    border-radius: 10px;
    position: relative; 
}

.close {
    color: #aaa;
    float: right;
    font-size: 28px;
    font-weight: bold;
    cursor: pointer;
    position: absolute;
    top: 10px;
    right: 15px; 
}

.close:hover,
.close:focus {
    color: black;
    text-decoration: none;
    cursor: pointer;
}

.form-group {
    margin-bottom: 15px;
}

.form-control {
    width: 100%;
    padding: 8px;
    box-sizing: border-box;
    border-radius: 5px;
    border: 1px solid #ccc;
}

.btn {
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

.add-icon {
    cursor: pointer;
    margin-top: 10px;
}

.add-icon:hover {
    color: #0056b3
}
</style>
