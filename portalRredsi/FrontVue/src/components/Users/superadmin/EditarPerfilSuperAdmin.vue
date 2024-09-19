<template>
    <div class="update-profile-container">
      <h2 class="title">Actualizar Perfil de Superadmin</h2>
  
      <!-- Mostrar mensaje de éxito o error -->
      <div v-if="message" class="success-message">{{ message }}</div>
      <div v-if="error" class="error-message">{{ error }}</div>
  
      <!-- Formulario para actualizar el perfil -->
      <form @submit.prevent="handleSubmit" class="update-form">
        <div class="form-group">
          <label for="nombres">Nombres:</label>
          <input
            id="nombres"
            type="text"
            v-model="userData.nombres"
            required
          />
        </div>
  
        <div class="form-group">
          <label for="apellidos">Apellidos:</label>
          <input
            id="apellidos"
            type="text"
            v-model="userData.apellidos"
            required
          />
        </div>
  
        <div class="form-group">
          <label for="correo">Correo:</label>
          <input
            id="correo"
            type="email"
            v-model="userData.correo"
            required
          />
        </div>
  
        <div class="form-group">
          <label for="telefono">Teléfono:</label>
          <input
            id="telefono"
            type="text"
            v-model="userData.telefono"
            required
          />
        </div>
  
        <button type="submit" class="submit-button bg-warning">Actualizar Perfil</button>
      </form>
    </div>
  </template>
  
  <script>
   import { updateUserProfile } from '../../../services/superadminService'; // Asegúrate de importar el servicio correctamente
  
  export default {
    props: {
      userId: {
        type: Number,
        required: true
      }
    },
    data() {
      return {
        // Datos del formulario
        userData: {
          nombres: "",
          apellidos: "",
          correo: "",
          telefono: ""
        },
        message: "", // Mensaje de éxito
        error: "" // Mensaje de error
      };
    },
    methods: {
      async handleSubmit() {
        try {
          // Llamar al servicio para actualizar el perfil
          const response = await updateUserProfile(this.userId, this.userData);
          this.message = response.mensaje; // Mostrar mensaje de éxito
          this.error = ""; // Limpiar errores previos
        } catch (err) {
          this.error = err.detail || "Error al actualizar el perfil"; // Mostrar mensaje de error
          this.message = ""; // Limpiar mensajes previos
        }
      }
    }
  };
  </script>
  
  <style scoped>
  .update-profile-container {
    max-width: 500px;
    margin: 0 auto;
    padding: 20px;
    background-color: #f9f9f9;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }
  
  .title {
    text-align: center;
    font-size: 24px;
    color: #333;
    margin-bottom: 20px;
  }
  
  .success-message {
    color: green;
    text-align: center;
    margin-bottom: 15px;
  }
  
  .error-message {
    color: red;
    text-align: center;
    margin-bottom: 15px;
  }
  
  .update-form {
    display: flex;
    flex-direction: column;
  }
  
  .form-group {
    margin-bottom: 15px;
  }
  
  .form-group label {
    display: block;
    font-size: 16px;
    margin-bottom: 5px;
    color: #333;
  }
  
  .form-group input {
    width: 100%;
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 14px;
  }
  
  .submit-button {
    padding: 10px;
    background-color: #28a745;
    color: white;
    border: none;
    border-radius: 4px;
    font-size: 16px;
    cursor: pointer;
  }
  
  .submit-button:hover {
    background-color: #218838;
  }
  </style>
  