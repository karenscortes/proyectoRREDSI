<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-xl-10 col-lg-10 col-md-12">
        <div class="section_title text-center mb-5">
          <h1>Perfil de Usuario</h1>
        </div>

        <!-- Spinner global -->
        <SpinnerGlobal v-if="loading" />

        <div class="big-screen" v-if="!loading">
          <div class="row text-center justify-content-center">
            <div class="col-lg-4 col-sm-3">
              <button @click="setActiveSection('datos_personales')" class="btn btn-outline-dark w-100 form-btn" :class="{'btn-active': isPressed, 'btn-inactive': !isPressed}">
                <strong class="font-weight-bold">
                  <i class="fas fa-user-secret"></i>
                </strong>
                Datos Personales
              </button>
            </div>
            <div class="col-lg-4 col-sm-3">
              <button @click="setActiveSection('datos_institucionales')" class="btn btn-outline-dark w-100 form-btn" :class="{'btn-active': isActive, 'btn-inactive': !isActive}">
                <strong class="font-weight-bold">
                  <i class="fas fa-university"></i>
                </strong>
                Datos Institucionales
              </button>
            </div>
            <div class="col-lg-4 col-sm-3">
              <button @click="setActiveSection('datos_academicos')" class="btn btn-outline-dark w-100 form-btn" :class="{'btn-active': isSelected, 'btn-inactive': !isSelected}">
                <strong class="font-weight-bold">
                  <i class="fas fa-graduation-cap"></i>
                </strong>
                Datos Académicos
              </button>
            </div>
          </div>

          <!-- Sección de datos personales -->
          <div v-if="activeSection === 'datos_personales'" class="form-section mt-5" id="datos_personales">
            <div class="d-flex align-items-center justify-content-center mb-4">
              <i class="fas fa-user-secret title-icon"></i>
              <h2>Datos Personales</h2>
            </div>
            <div class="title-line"></div>
            <form @submit.prevent="submitPersonalData()" class="row my-5 font-weight-bold text-dark">
              <div class="form-row justify-content-center mb-3">
                <div class="form-group col-md-5 me-3">
                  <label for="inputName">Nombres:</label>
                  <input type="text" v-model="formData.personal.nombres" class="form-control" id="inputName" required/>
                </div>
                <div class="form-group col-md-5 mb-3">
                  <label for="inputLastname">Apellidos:</label>
                  <input type="text" v-model="formData.personal.apellidos" class="form-control" id="inputLastname" required />
                </div>
              </div>
              <div class="form-row justify-content-center mb-3">
                <div class="form-group col-md-5 me-3">
                  <label for="inputDocumentType">Tipo de documento:</label>
                  <select :disabled="tipoDocumento != ''" id="inputDocumentType" v-model="tipoDocumento" type="select" class="form-control text-dark custom-select" required>
                    <option disabled selected v-if="tipoDocumento=='Seleccione una opción'">{{tipoDocumento}}</option>
                    <option v-for="opc in documentsTypes" :key="opc.id_tipo_documento" :value="opc.nombre">{{ opc.nombre }}</option>
                  </select>
                </div>
                <div class="form-group col-md-5">
                  <label for="inputDocumentNumber">N° de Documento:</label>
                  <input :disabled="formData.personal.documento != null" type="text" v-model="formData.personal.documento" class="form-control" id="inputDocumentNumber" />
                </div>
              </div>
              <div class="form-row justify-content-center mb-5">
                <div class="form-group col-md-10" style="padding:0;margin:0">
                  <label for="inputEmail">Correo:</label>
                  <input type="email" v-model="formData.personal.correo" class="form-control p-1" id="inputEmail" placeholder="usuario@gmail.com" required/>
                </div>
              </div>
              <div class="text-center mb-5">
                <button type="button" class="btn form-btn rounded-circle btn-outline-dark mx-2" @click="showModal()"><i class="fa-solid fa-lock"></i></button>
              </div>
              <div class="text-center">
                <button type="submit" class="btn btn-warning font-weight-bold text-dark w-25">Guardar</button>
              </div>
            </form>
          </div>

          <!-- Sección de datos institucionales -->
          <div v-if="activeSection === 'datos_institucionales'" class="form-section mt-5" id="datos_institucionales">
            <div class="d-flex align-items-center justify-content-center mb-4">
              <i class="fas fa-university title-icon"></i>
              <h2>Datos Institucionales</h2>
            </div>
            <div class="title-line"></div>
            <form @submit.prevent="submitInstitutionalData()" class="row my-5 font-weight-bold text-dark">
              <div class="form-row justify-content-center mb-3">
                <div class="form-group col-md-5 me-3">
                  <label for="inputPlaceName">Institución educativa:</label>
                  <select id="inputPlceName" v-model="selectedInstitution" type="select" class="form-control text-dark custom-select" required>
                    <option disabled selected v-if="selectedInstitution=='Seleccione una opción'">{{selectedInstitution}}</option>
                    <option v-for="opc in instituciones" :key="opc.id_tipo_documento" :value="opc.nombre">{{ opc.nombre }}</option>
                  </select>
                </div>
                <div class="form-group col-md-5 mb-3">
                  <label for="inputResearchGroup">Grupo de Investigación:</label>
                  <input type="text" v-model="formData.institucional.grupo_investigacion" class="form-control" id="inputResearchGroup" required />
                </div>
              </div>
              <div class="form-row justify-content-center mb-5">
                <div class="form-group col-md-10" style="padding:0;margin:0">
                  <label for="inputResearchLab">Nombre del Semillero:</label>
                  <input type="text" v-model="formData.institucional.semillero" class="form-control" id="inputResearchLab" />
                </div>
              </div>
              <div class="form-row justify-content-center mb-5">
                <div class="form-group col-md-5 me-3">
                    <label for="inputKnowledgeArea">Area de Conocimiento:</label>
                    <select id="inputKnowledgeArea" v-model="primeraArea" type="select" class="form-control text-dark custom-select" required>
                      <option disabled selected v-if="primeraArea=='Seleccione una opción'">{{primeraArea}}</option>
                      <option v-for="opc in areasConocimiento" :key="opc.id_area_conocimiento" :value="opc.nombre">{{ opc.nombre }}</option>
                    </select>
                </div>
                <div class="form-group col-md-5">
                    <label for="inputAnotherArea">Otra Area:</label>
                    <select id="inputAnotherArea"  v-model="segundaArea" type="select" class="form-control text-dark custom-select" required>
                      <option disabled selected v-if="segundaArea=='Seleccione una opción'">{{segundaArea}}</option>
                      <option v-for="opc in areasConocimiento" :key="opc.id_area_conocimiento" :value="opc.nombre">{{ opc.nombre }}</option>
                    </select>
                </div>                                   
              </div> 
              <div class="text-center">
                <button type="submit" class="btn btn-warning font-weight-bold text-dark w-25">Guardar</button>
              </div> 
            </form>
          </div>

          <!-- Sección de datos académicos -->
          <div v-if="activeSection === 'datos_academicos'" class="form-section mt-5" id="datos_academicos">
            <div class="d-flex align-items-center justify-content-center mb-4">
              <i class="fas fa-graduation-cap title-icon"></i>
              <h2>Datos Académicos</h2>
            </div>
            <div class="title-line"></div>
            <form @submit.prevent="submitCertificates()" class="row my-5 font-weight-bold text-dark">
              <div class="form-row justify-content-center mb-3">
                <div class="form-group col-md-5 ms-md-4 ms-xs-5">
                  <label for="inputUndergraduateDegree">Título Pregrado:</label>
                  <!-- para editar o insertar -->
                  <div class="row me-3" v-if="formData.academico.pregrado == '' || editPregrado">
                    <div class="col-10">
                      <input type="text" class="form-control w-100" id="inputUndergraduateDegree" v-model="titulo1" />
                    </div>
                    <div class="col-1">
                      <label class="items-center pt-1 ps-0text-black">
                        <i class="fa-solid fa-square-plus fs-4 certificates_icons"></i>
                        <input  type="file" class="d-none d-print-block" @change="handleFileChange('pregrado',$event)" />
                      </label>
                    </div>
                  </div>
                  <!-- para visualizar -->
                  <div class="row me-3" v-else >
                    <div class="col-10">
                      <a :href="'https://proyectorredsi-whpk.onrender.com/'+formData.academico.pregrado.url_titulo" target="_blank">{{ formData.academico.pregrado.nombre_titulo }}</a>
                    </div>
                    <div class="col-1">
                      <button class="btn items-center pt-1 ps-0 text-black" style="background:#f8f9fa;" @click="editPregrado = true">
                        <i class="fas fa-edit fa-2x fs-5 certificates_icons"></i>
                      </button>
                    </div>
                  </div>
                </div>
                <div class="form-group col-md-5 mb-3 ms-md-3 ms-xs-5">
                  <label for="inputPostgraduateDiploma">Título de Especialización:</label>
                  <!-- para editar o insertar -->
                  <div class="row me-3" v-if="formData.academico.especializacion == '' || editEpecializacion">
                    <div class="col-10">
                      <input type="text" class="form-control w-100" id="inputPostgraduateDiploma" v-model="titulo2" />
                    </div>
                    <div class="col-1">
                      <label class="items-center pt-1 ps-0 text-black">
                        <i class="fa-solid fa-square-plus fs-4 certificates_icons"></i>
                        <input  type="file" class="d-none d-print-block" @change="handleFileChange('especializacion',$event)" />
                      </label>
                    </div>
                  </div>
                  <!-- para visualizar -->
                  <div class="row me-3" v-else >
                    <div class="col-10">
                      <a :href="'https://proyectorredsi-whpk.onrender.com/'+formData.academico.especializacion.url_titulo" target="_blank">{{ formData.academico.especializacion.nombre_titulo }}</a>
                    </div>
                    <div class="col-1">
                      <button class="btn items-center pt-1 ps-0 text-black" style="background:#f8f9fa;" @click="editEpecializacion = true">
                        <i class="fas fa-edit fa-2x fs-5 certificates_icons"></i>
                      </button>
                    </div>
                  </div>
                </div>
              </div>
              <div class="form-row justify-content-center mb-3">
                <div class="form-group col-md-5 ms-md-4 ms-xs-5">
                  <label for="inputMasterDegree">Título de Maestría:</label>
                  <!-- para editar o insertar -->
                  <div class="row me-3" v-if="formData.academico.maestria == '' || editMaestria">
                    <div class="col-10">
                      <input type="text" class="form-control w-100" id="inputMasterDegree" v-model="titulo3"/>
                    </div>
                    <div class="col-1">
                      <label class="items-center pt-1 ps-0 text-black">
                        <i class="fa-solid fa-square-plus fs-4 certificates_icons"></i>
                        <input  type="file" class="d-none d-print-block" @change="handleFileChange('maestria',$event)" />
                      </label>
                    </div>
                  </div>
                  <!-- para visualizar -->
                  <div class="row me-3" v-else >
                    <div class="col-10">
                      <a :href="'https://proyectorredsi-whpk.onrender.com/'+formData.academico.maestria.url_titulo" target="_blank">{{ formData.academico.maestria.nombre_titulo }}</a>
                    </div>
                    <div class="col-1">
                      <button class="btn items-center pt-1 ps-0 text-black" style="background:#f8f9fa;" @click="editMaestria = true">
                        <i class="fas fa-edit fa-2x fs-5 certificates_icons"></i>
                      </button>
                    </div>
                  </div>                        
                </div>
                <div class="form-group col-md-5 mb-5 ms-md-3 ms-xs-5">
                  <label for="inputPhD">Título de doctorado:</label>
                  <!-- para editar o insertar -->
                  <div class="row me-3" v-if="formData.academico.doctorado == '' || editDoctorado">
                    <div class="col-10">
                      <input type="text" class="form-control w-100" id="inputPhD" v-model="titulo4"/>
                    </div>
                    <div class="col-1">
                      <label class="items-center pt-1 ps-0 text-black">
                        <i class="fa-solid fa-square-plus fs-4 certificates_icons"></i>
                        <input  type="file" class="d-none d-print-block" @change="handleFileChange('doctorado',$event)" />
                      </label>
                    </div>
                  </div>
                  <!-- para visualizar -->
                  <div class="row me-3" v-else >
                    <div class="col-10">
                      <a :href="'https://proyectorredsi-whpk.onrender.com/'+formData.academico.maestria.url_titulo" target="_blank">{{ formData.academico.doctorado.nombre_titulo }}</a>
                    </div>
                    <div class="col-1">
                      <button class="btn items-center pt-1 ps-0 text-black" style="background:#f8f9fa;" @click="editDoctorado = true">
                        <i class="fas fa-edit fa-2x fs-5 certificates_icons"></i>
                      </button>
                    </div>
                  </div>        
                </div>
              </div>
              <div class="text-center">
                <button type="submit" class="btn btn-warning font-weight-bold text-dark w-25">Guardar</button>
              </div> 
            </form>
          </div>
        </div>


        <!-- Accordion -->
        <div class="accordion pt-5" id="accordionExample">
          <!-- #1 -->
          <div class="card p-2 border border-dark">
            <div id="headingOne">
                <button class="btn btn-block toggle-button" type="button" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
                  <i class="fas fa-user-secret"></i> Datos Personales
                </button>
            </div> 
            <div id="collapseOne" class="collapse show" aria-labelledby="headingOne" data-parent="#accordionExample">
              
              <div class="card-body my-3 font-weight-bold text-dark">
                  <div class="title-line mb-4"></div> 
                  <form @submit.prevent="submitPersonalData()">
                      <div class="form-row">
                          <div class="form-group col-md-6">
                            <label for="inputName">Nombres:</label>
                            <input type="text" class="form-control" id="inputName" v-model="formData.personal.nombres">
                          </div>
                          <div class="form-group col-md-6">
                            <label for="inputLastname">Apellidos:</label>
                            <input type="text" class="form-control" id="inputLastname" v-model="formData.personal.apellidos">
                          </div>
                      </div>
                      <div class="form-row">
                          <div class="form-group col-md-6">
                              <label for="inputDocumentType">Tipo de documento:</label>
                              <select :disabled="tipoDocumento != ''"  id="inputDocumentType" v-model="tipoDocumento" type="select" class="form-control text-dark custom-select" required>
                                <option disabled selected v-if="tipoDocumento=='Seleccione una opción'">{{tipoDocumento}}</option>
                                <option v-for="opc in documentsTypes" :key="opc.id_tipo_documento" :value="opc.nombre">{{ opc.nombre }}</option>
                              </select>
                          </div>
                        
                          <div class="form-group col-md-6">
                              <label for="inputCity">N° de Documento:</label>
                              <input :disabled="formData.personal.documento != null" type="text" class="form-control" id="inputCity" v-model="formData.personal.documento">
                          </div>
                      </div>
                      <div class="form-group mb-5">
                          <label for="inputAddress">Correo:</label>
                          <input type="email" class="form-control" id="inputAddress" placeholder="usuario@gmail.com" v-model="formData.personal.correo">
                      </div>
                      <div class="text-center mb-5">
                        <button type="button" class="btn form-btn rounded-circle btn-outline-dark mx-2" @click="showChangePasswordModal"><i class="fa-solid fa-lock"></i></button>
                      </div>
                      <div class="text-center">
                        <button type="submit" class="btn btn-warning font-weight-bold text-dark w-25 ">Guardar</button>
                      </div>                                                   
                  </form>                          
              </div>
            </div>
          </div>
          <!-- #2 -->
          <div class="card p-2 border border-dark">
            <div id="headingTwo">
              <h2 class="mb-0">
                <button class="btn btn-block toggle-button collapsed" type="button" data-toggle="collapse" data-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
                  <i class="fas fa-university"></i> Datos Institucionales
                </button>
              </h2>
            </div>
            <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordionExample">
              <div class="card-body my-3 font-weight-bold text-dark">
                  <div class="title-line mb-4"></div> 
                  <form @submit.prevent="submitInstitutionalData()" >
                      <div class="form-row">
                          <div class="form-group col-md-6">
                            <label for="inputPlaceName">Institución educativa:</label>
                            <select id="inputPlceName" v-model="selectedInstitution" type="select" class="form-control text-dark custom-select" required>
                              <option disabled selected v-if="selectedInstitution=='Seleccione una opción'">{{selectedInstitution}}</option>
                              <option v-for="opc in instituciones" :key="opc.id_tipo_documento" :value="opc.nombre">{{ opc.nombre }}</option>
                            </select>
                          </div>
                          <div class="form-group col-md-6">
                            <label for="inputResearchGroup">Grupo de Investigación:</label>
                            <input type="text" class="form-control" id="inputSearchGroup" v-model="formData.institucional.grupo_investigacion" required>
                          </div>
                      </div>
                      <div class="form-group">
                          <label for="inputResearchLab">Nombre del Semillero:</label>
                          <input type="text" class="form-control" id="inputResearchLab" v-model="formData.institucional.semillero">
                      </div> 
                      <div class="form-group row justify-content-center">
                        <label for="inputKnowledgeArea" class="col-md-10 mx-4">Area de Conocimiento:</label>
                        <div class="col-md-10">
                          <select id="inputKnowledgeArea" v-model="formData.institucional.id_primer_area_conocimiento" type="select" class="form-control text-dark custom-select" required>
                            <option disabled selected v-if="primeraArea=='Seleccione una opción'">{{primeraArea}}</option>
                            <option v-for="opc in areasConocimiento" :key="opc.id_area_conocimiento" :value="opc.nombre">{{ opc.nombre }}</option>
                          </select>
                        </div> 
                    </div>
                    <div class="form-group row justify-content-center">
                        <label for="inputAnotherArea" class="col-md-10 mx-4">Otra Area:</label>
                        <div class="col-md-10">
                          <select id="inputAnotherArea"  v-model="formData.institucional.segunda_area" type="select" class="form-control text-dark custom-select" required>
                            <option disabled selected v-if="segundaArea=='Seleccione una opción'">{{segundaArea}}</option>
                            <option v-for="opc in areasConocimiento" :key="opc.id_area_conocimiento" :value="opc.nombre">{{ opc.nombre }}</option>
                          </select>
                        </div>
                    </div>
                    <div class="text-center">
                      <button type="submit" class="btn btn-warning font-weight-bold text-dark w-25 ">Guardar</button>
                    </div>                                 
                  </form>
              </div>
            </div>
          </div>
          <!-- #3 -->
          <div class="card  p-2 border border-dark">
            <div id="headingThree">
              <h2 class="mb-0">
                <button class="btn btn-block toggle-button collapsed" type="button" data-toggle="collapse" data-target="#collapseThree" aria-expanded="false" aria-controls="collapseThree">
                  <i class="fas fa-graduation-cap"></i> Datos Academicos
                </button>
              </h2>
            </div>
            <div id="collapseThree" class="collapse" aria-labelledby="headingThree" data-parent="#accordionExample">
              <div class="card-body my-3 font-weight-bold text-dark">
                  <div class="title-line mb-4"></div> 
                  <form @submit.prevent="submitCertificates()">           
                    <div class="form-group row justify-content-center">              
                      <label for="inputUndergraduateDegree" class="col-4">Titulo Pregrado:</label>
                      <!-- Editar o Insertar-->
                      <div class="d-inline-flex col-6" v-if="formData.academico.pregrado == '' || editPregrado" >
                          <input type="text" class="form-control w-100" id="inputUndergraduateDegree" v-model="titulo1"/>
                          <label class="items-center p-1 text-black ml-2">
                              <i class="fa-solid fa-square-plus fs-4 certificates_icons"></i>
                              <input type='file' class="d-none d-print-block" />
                          </label>
                      </div>
                      <!-- Visualizar-->
                      <div class="d-inline-flex col-6" v-else>
                        <a :href="'https://proyectorredsi-whpk.onrender.com/'+formData.academico.pregrado.url_titulo" target="_blank">{{ formData.academico.pregrado.nombre_titulo }}</a>
                        <label class="items-center pt-1 ps-3 text-black ml-4" @click="editPregrado = true">
                          <i class="fas fa-edit fa-2x fs-5 certificates_icons"></i>
                        </label>
                      </div>
                    </div>
                    <div class="form-group row justify-content-center">
                        <label for="inputPostgraduateDiploma" class="col-4">Titulo de Especialización:</label>
                        <!-- Editar o Insertar-->
                      <div class="d-inline-flex col-6" v-if="formData.academico.especializacion == '' || editEpecializacion" >
                        <input type="text" class="form-control w-100" id="inputPostgraduateDiploma" v-model="titulo2" />
                        
                        <label class="items-center p-1 text-black ml-2">
                            <i class="fa-solid fa-square-plus fs-4 certificates_icons"></i>
                            <input type='file' class="d-none d-print-block" />
                        </label>
                      </div>
                      <!-- Visualizar-->
                      <div class="d-inline-flex col-6" v-else>
                        <a :href="'https://proyectorredsi-whpk.onrender.com/'+formData.academico.especializacion.url_titulo" target="_blank">{{ formData.academico.especializacion.nombre_titulo }}</a>
                        <label class="items-center pt-1 ps-3 text-black ml-4" @click="editEpecializacion = true">
                          <i class="fas fa-edit fa-2x fs-5 certificates_icons"></i>
                        </label>
                      </div>        
                    </div>
                    <div class="form-group row justify-content-center">
                      <label for="inputMasterDegree" class="col-4">Titulo de Maestría:</label>
                        <!-- Editar o Insertar-->
                      <div class="d-inline-flex col-6" v-if="formData.academico.maestria == '' || editMaestria" >
                        <input type="text" class="form-control w-100" id="inputMasterDegree" v-model="titulo3"/>
                        <label class="items-center p-1 text-black ml-2">
                            <i class="fa-solid fa-square-plus fs-4 certificates_icons"></i>
                            <input type='file' class="d-none d-print-block" />
                        </label>
                      </div>
                      <!-- Visualizar-->
                      <div class="d-inline-flex col-6" v-else>
                        <a :href="formData.academico.maestria.url_titulo" target="_blank">{{ formData.academico.maestria.nombre_titulo }}</a>
                        <label class="items-center pt-1 ps-3 text-black ml-4" @click="editMaestria = true">
                          <i class="fas fa-edit fa-2x fs-5 certificates_icons"></i>
                        </label>
                      </div>
                        
                    </div>                            
                    <div class="form-group row justify-content-center">
                      <label for="inputPhD" class="col-4">Titulo de Doctorado:</label>
                        <!-- Editar o Insertar-->
                      <div class="d-inline-flex col-6" v-if="formData.academico.doctorado == '' || editDoctorado" >
                        <input  type="text" class="form-control w-100" id="inputPhD" v-model="titulo4" />
                       
                        <label class="items-center p-1 text-black ml-2">
                            <i class="fa-solid fa-square-plus fs-4 certificates_icons"></i>
                            <input type='file' class="d-none d-print-block" />
                        </label>
                      </div>
                      <!-- Visualizar-->
                      <div class="d-inline-flex col-6" v-else>
                        <a :href="'https://proyectorredsi-whpk.onrender.com/'+formData.academico.doctorado.url_titulo" target="_blank">{{ formData.academico.doctorado.nombre_titulo }}</a>
                        <label class="items-center pt-1 ps-3 text-black ml-4" @click="editDoctorado = true">
                          <i class="fas fa-edit fa-2x fs-5 certificates_icons"></i>
                        </label>
                      </div>
                    </div>
                    <div class="text-center">
                      <button type="submit" class="btn btn-warning font-weight-bold text-dark w-25 ">Guardar</button>
                    </div>                                                                                  
                  </form>
              </div>
            </div>
          </div>  
        </div>
      </div>
    </div>
  </div>

  <!-- Modal -->
  <ChangePasswordModal v-if="isModalOpen" @close="closeModal()" :email="formData.personal.correo" />
</template>

<script>
import { createInstitutionalData, getInstitutionalDetails,updateInstitutionalData,updateUserProfile,createUpdateRecords,insertCertificatesFiles} from '../../services/UsuarioService';
import { getAllTiposDocumento } from '../../services/TipoDocumentoService';
import { useAuthStore } from '@/store';
import { getCertificatesById } from '@/services/postulacionService';
import { getAreasConocimiento } from '@/services/administradorService';
import {getAllInstituciones} from '@/services/institucionesService';
import ChangePasswordModal from './ChangePasswordModal.vue';
import { useToastUtils } from '@/utils/toast';
import {ref} from 'vue';
import SpinnerGlobal from '../UI/SpinnerGlobal.vue';


export default {
  components: {
    ChangePasswordModal,
  },
  data() {
    return {
      editInstitutionalData:false,
      next:'datos_institucionales',
      previous:'',
      activeSection: 'datos_personales',
      editPregrado: false,
      editMaestria: false,
      editEpecializacion: false,
      editDoctorado: false,
      isPressed:true,
      isActive:false,
      isSelected:false,
      isModalOpen:false,
      loading: false,
      formData: {
        personal: {
          id_tipo_documento: '',
          documento: '',
          nombres: '',
          apellidos: '',
          correo: '',
        },
        institucional: {
          id_usuario:'',
          id_institucion: '',
          semillero: '',
          grupo_investigacion: '',
          id_primera_area_conocimiento:'',
          id_segunda_area_conocimiento:'',
        },
        academico: {
          pregrado: '',
          especializacion: '',
          maestria: '',
          doctorado: '',
        },
      },
      tipoDocumento:'Seleccione una opción',
      selectedInstitution:'Seleccione una opción',
      primeraArea:'Seleccione una opción',
      segundaArea:'Seleccione una opción',
      titulo1:'',
      titulo2:'',
      titulo3:'',
      titulo4:'',
      pregradoFile: null,
      especializacionFile: null,
      maestriaFile: null,
      doctoradoFile: null,
      areasConocimiento: [],
      documentsTypes:[],
      instituciones:[],
      nombres_titulos:{}
    };
  },
  setup() {
        const authStore = useAuthStore();

        const user = ref(authStore.user);

        return {
            user,
        };
  },
  methods: {
    ... useToastUtils(),
    //Controlador de las secciones activas
    setActiveSection(section) {
      this.activeSection = section;

      if(section == 'datos_personales'){
        this.next = 'datos_institucionales';
        this.isPressed = true;
        this.isActive= false;
        this.isSelected = false;

      }else if(section == 'datos_institucionales'){
        this.next = 'datos_academicos';
        this.previous = 'datos_personales';
        this.isPressed = false;
        this.isActive= true;
        this.isSelected = false;
      }else if(section == 'datos_academicos'){
        this.previous = 'datos_institucionales';
        this.isPressed = false;
        this.isActive= false;
        this.isSelected = true;
      }
    },
    
    //Se obtienen los tipos de documentos
    async getDocumentsTypes(){

      //todas la opciones
      const response = await getAllTiposDocumento();
      this.documentsTypes = response.data;

      //tipo de doc actual
      this.documentsTypes.forEach(tipo => {
        if (tipo.id_tipo_documento === this.user.id_tipo_documento) {
          this.tipoDocumento = tipo.nombre;
        }
      });

    },

    //Se obtienen los datos academicos
    async getInstitutionalData(){

        //Se obtienen todas las  Areas de Conocimiento
        const responseAreasConocimiento = await getAreasConocimiento();
        this.areasConocimiento = responseAreasConocimiento.data;


        //Se obtienen todas las instituciones
        const responseInstituciones = await getAllInstituciones();
          this.instituciones = responseInstituciones.data;
        
        const response_datos_academicos = await getInstitutionalDetails();
        if(response_datos_academicos != null){
          this.editInstitutionalData=true;

          this.formData.institucional.id_usuario = response_datos_academicos.data.id_usuario;
          this.formData.institucional.id_institucion = response_datos_academicos.data.id_institucion ;
          this.formData.institucional.grupo_investigacion = response_datos_academicos.data.grupo_investigacion;
          this.formData.institucional.semillero = response_datos_academicos.data.semillero;
          this.formData.institucional.id_primera_area_conocimiento = response_datos_academicos.data.id_primera_area_conocimiento;
          this.formData.institucional.id_segunda_area_conocimiento = response_datos_academicos.data.id_segunda_area_conocimiento;

          //Se obtiene Area de conocimiento especifica
          this.areasConocimiento.forEach(tipo => {
            if (tipo.id_area_conocimiento === response_datos_academicos.data.id_primera_area_conocimiento) {
              this.primeraArea= tipo.nombre;
            }else if(tipo.id_area_conocimiento === response_datos_academicos.data.id_segunda_area_conocimiento){
              this.segundaArea = tipo.nombre;
            }

            
            //Se obtiene el nombre de la institución actual
            this.instituciones.forEach(cur_opc => {
              if (cur_opc.id_institucion === response_datos_academicos.data.id_institucion) {
                this.selectedInstitution = cur_opc.nombre
              }
            });
          });
        }
    },

    // Se obtienen los titulos 
    async getCertificates(){
      
      try {
        const responseTitulos = await getCertificatesById(this.user.id_usuario);
        const titulos = responseTitulos.data;

        this.editPregrado=false;
        this.editEpecializacion=false;
        this.editMaestria=false;
        this.editDoctorado=false;

        for (let i = 0; i < titulos.length; i++) {
          if (titulos[i].nivel == "pregrado") {
            this.formData.academico.pregrado = titulos[i];
            this.titulo1 = titulos[i].nombre_titulo;
          }else if (titulos[i].nivel == "especializacion") {
            this.formData.academico.especializacion = titulos[i];
            this.titulo2 = titulos[i].nombre_titulo;
          }else if (titulos[i].nivel == "doctorado") {
            this.formData.academico.doctorado = titulos[i];
            this.titulo4 = titulos[i].nombre_titulo;
          }else if (titulos[i].nivel == "maestria") {
            this.formData.academico.maestria = titulos[i];
            this.titulo3 = titulos[i].nombre_titulo;
          }
        }
      } catch (error) {
        console.error(error);
      }
    },
    
    //Controlador de archivos academicos
    handleFileChange(tipo, event) {
      
      if (tipo == 'pregrado') {
        this.pregradoFile = event.target.files[0];
      } else if (tipo == 'especializacion') {
        this.especializacionFile = event.target.files[0];
      } else if (tipo == 'maestria') {
        this.maestriaFile = event.target.files[0];
      }else if(tipo == 'doctorado'){
        this.doctoradoFile= event.target.files[0];
      }
    },

    async submitPersonalData(){

      this.documentsTypes.forEach(tipo => {
        if (tipo.nombre === this.formData.personal.id_tipo_documento) {
          this.formData.personal.id_tipo_documento = tipo.id_tipo_documento;
        }
      });

      try{
        const updated_data = await updateUserProfile(this.user.id_usuario, this.formData.personal);
        this.showSuccessToast('Actualización exitosa');

          // Obtenemos la información del usuario en localStorage
          const userInStorage = JSON.parse(localStorage.getItem('user')); 
          console.log("DATOS:");

          console.log(userInStorage.apellidos)
          console.log(updated_data.apellidos)
          // Actualizamos los datos del usuario
          userInStorage.id_tipo_documento = updated_data.id_tipo_documento;
          userInStorage.documento = updated_data.documento;
          userInStorage.nombres = updated_data.nombres;
          userInStorage.apellidos=updated_data.apellidos;
          userInStorage.correo = updated_data.correo;
          localStorage.setItem('user', JSON.stringify(userInStorage)); 
  
          this.user.value = { ...userInStorage };

          this.formData = {
            ...this.formData,
            personal: {
              id_tipo_documento: updated_data.id_tipo_documento,
              documento: updated_data.documento,
              nombres: updated_data.nombres,
              apellidos: updated_data.apellidos,
              correo: updated_data.correo,
            },
          };
      }catch {
        this.showErrorToast('Error al actualizar datos personales');
      }
      
    },

    async submitInstitutionalData(){
      this.formData.institucional.id_usuario = this.user.id_usuario;

      this.instituciones.forEach(cur_opc => {
          if (cur_opc.nombre === this.selectedInstitution) {
            this.formData.institucional.id_institucion = cur_opc.id_institucion
          }
      });

      this.areasConocimiento.forEach(tipo => {
          if (tipo.nombre === this.primeraArea) {
            this.formData.institucional.id_primera_area_conocimiento = tipo.id_area_conocimiento;
          }else if(tipo.nombre === this.segundaArea){
            this.formData.institucional.id_segunda_area_conocimiento = tipo.id_area_conocimiento;
          }
        });

      if(this.editInstitutionalData){
        try{
          const updated_data = await updateInstitutionalData(this.user.id_usuario,this.formData.institucional);
          this.showSuccessToast('Actualización exitosa');
          this.getInstitutionalData();
        }catch{
          this.showErrorToast('Error al actualizar datos institucionales');
        }
        
      }else{
        try{
          console.log("objecto:");
          console.log(this.formData.institucional);
          await createInstitutionalData(this.formData.institucional);
          this.showSuccessToast('Los datos institucionales se registraron exitosamente');
          this.getInstitutionalData();
        }catch{
          this.showErrorToast('Error al actualizar datos institucionales');
        }
      }

    },

    async submitCertificates(){

      this.nombres_titulos['pregrado'] = this.titulo1;
      this.nombres_titulos['especializacion'] = this.titulo2;
      this.nombres_titulos['maestria'] = this.titulo3;
      this.nombres_titulos['doctorado'] = this.titulo4;
      
      try{
        await createUpdateRecords(this.user.id_usuario,this.nombres_titulos);

        if(this.pregradoFile !== null || this.especializacionFile !== null || this.maestriaFile !== null || this.doctoradoFile !== null){
          await insertCertificatesFiles(this.user.id_usuario,this.pregradoFile,this.especializacionFile,this.maestriaFile,this.doctoradoFile);
        }

        this.showSuccessToast('Los datos académicos fueron procesados con éxito');
        this.getCertificates();
      }catch{
        this.showErrorToast('Error al procesar datos académicos');
      }
    },
    //Controladores de Modal
    showModal(){
      this.isModalOpen = true;
    },
    closeModal(){
      this.isModalOpen = false;
    }
  },
  mounted() {
    this.getDocumentsTypes();
    this.getInstitutionalData();
    this.getCertificates();
    
    const user = JSON.parse(localStorage.getItem('user')); 
    this.formData.personal = {
      id_tipo_documento: user.id_tipo_documento || '',
      documento: user.documento || '',
      nombres: user.nombres || '',
      apellidos: user.apellidos || '',
      correo: user.correo || '',
    };
  },
};
</script>
<style scoped>
.form-btn{
  background: white;
}
.form-btn:hover{
  background: #ffb606;
  color: white;
  border: none;
}

.form-btn:active{
  background: #ffb606;
  color: white;
  border: none;
}

.btn-active{
  background: #ffb606;
  color: white;
  border: none;
}
.btn-inactive{
  background: white;
}

.form-section{
  margin: 0;
  padding: 40px;
  max-width: 100%;
}

a
{
	display: inline;
	position: relative;
	color: #ffb606;
	border-bottom: solid 1px #ffb606;
	-webkit-transition: all 200ms ease;
	-moz-transition: all 200ms ease;
	-ms-transition: all 200ms ease;
	-o-transition: all 200ms ease;
	transition: all 200ms ease;
}
a:active
{
	position: relative;
	color: #ffb606;
}
a:hover
{
	color: #FFFFFF;
	background: #ffb606;
}
.certificates_icons:hover{
	color: #ffb606;
}

.accordion{
  display: none;
}

.title-line {
border-top: 2px solid rgb(255, 182, 6);
margin-top: -10px;
}

.form-section h2 {
color: rgb(255, 182, 6);
text-align: center;
}

.form-section .title-icon {
color: rgb(255, 182, 6);
margin-right: 10px;
font-size: 1.5rem;
margin-bottom: 10px;
}

.toggle-button{
  background: #f8f9fa;
  
}


@media only screen  and (max-width:767px){
.big-screen{
      display: none;
  }
  .accordion{
      display: block;
  }

  .card{
      width: 100%;
      text-align: left;
      text-decoration: none;
      background-color: #f7f7f7;
      border: 1px solid black;
      margin-bottom: 2rem;
  }

  .card button{
      font-weight: 700;
      text-align: center;
  }

  .toggle-button:not(.collapsed) {
      color: rgb(255, 182, 6);
  }

} 
</style>
