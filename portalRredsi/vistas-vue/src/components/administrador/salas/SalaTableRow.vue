<template>
  <div class="container pt-5">
    <div class="row mb-5 mt-2">
      <div class="col">
        <div class="section_title text-center">
          <h1>Gestionar Salas</h1>
        </div>
      </div>
    </div>
    <!-- Buscador y añadir sala -->
    <div class="row mb-4">
      <div
        class="col-12 divloco col-md-6 d-flex justify-content-start mb-3 mb-md-0"
      >
        <button
          class="btn btn-warning w-sm-100 w-75 font-weight-bold"
          data-toggle="modal"
          data-target="#addSalaModal"
        >
          Crear sala
        </button>
      </div>
      <div class="col-12 col-md-6 d-flex justify-content-end">
        <div class="d-flex w-100">
          <input
            type="text"
            id="busqueda"
            class="form-control mr-2"
            placeholder="Buscar..."
          />
          <button class="btn btn-warning font-weight-bold">Buscar</button>
        </div>
      </div>
    </div>

    <!-- Tabla -->
    <div class="table-responsive tablaloca">
      <table
        id="basic-datatables"
        class="display table table-striped table-hover text-dark"
      >
        <thead style="background: rgb(255, 182, 6)">
          <tr>
            <th>Número de sala</th>
            <th>Area de conocimiento</th>
            <th>Delegado asignado</th>
            <th>Editar</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td style="font-size: 16px">ABC2351</td>
            <td style="font-size: 16px">Ciencias naturales</td>
            <td style="font-size: 16px">Pepe Rodrigo Sanchez</td>
            <td>
              <a
                type="button"
                data-toggle="modal"
                data-target="#updateSalaModal"
                ><i class="far fa-edit" style="font-size: 25px"></i
              ></a>
            </td>
          </tr>
          <tr>
            <td style="font-size: 16px">ABC2352</td>
            <td style="font-size: 16px">Biología</td>
            <td style="font-size: 16px">Ana María Gómez</td>
            <td>
              <a
                type="button"
                data-toggle="modal"
                data-target="#updateSalaModal"
                ><i class="far fa-edit" style="font-size: 25px"></i
              ></a>
            </td>
          </tr>
          <tr>
            <td style="font-size: 16px">ABC2353</td>
            <td style="font-size: 16px">Química</td>
            <td style="font-size: 16px">Carlos Ruiz</td>
            <td>
              <a
                type="button"
                data-toggle="modal"
                data-target="#updateSalaModal"
                ><i class="far fa-edit" style="font-size: 25px"></i
              ></a>
            </td>
          </tr>
          <tr>
            <td style="font-size: 16px">ABC2354</td>
            <td style="font-size: 16px">Historia</td>
            <td style="font-size: 16px">Lucía Fernández</td>
            <td>
              <a
                type="button"
                data-toggle="modal"
                data-target="#updateSalaModal"
                ><i class="far fa-edit" style="font-size: 25px"></i
              ></a>
            </td>
          </tr>
          <tr>
            <td style="font-size: 16px">ABC2355</td>
            <td style="font-size: 16px">Geografía</td>
            <td style="font-size: 16px">Andrés Bustamante</td>
            <td>
              <a
                type="button"
                data-toggle="modal"
                data-target="#updateSalaModal"
                ><i class="far fa-edit" style="font-size: 25px"></i
              ></a>
            </td>
          </tr>
          <tr>
            <td style="font-size: 16px">ABC2356</td>
            <td style="font-size: 16px">Educación Física</td>
            <td style="font-size: 16px">Elena Martínez</td>
            <td>
              <a
                type="button"
                data-toggle="modal"
                data-target="#updateSalaModal"
                ><i class="far fa-edit" style="font-size: 25px"></i
              ></a>
            </td>
          </tr>
          <tr>
            <td style="font-size: 16px">ABC2357</td>
            <td style="font-size: 16px">Filosofía</td>
            <td style="font-size: 16px">Jorge Villalba</td>
            <td>
              <a
                type="button"
                data-toggle="modal"
                data-target="#updateSalaModal"
                ><i class="far fa-edit" style="font-size: 25px"></i
              ></a>
            </td>
          </tr>
          <tr>
            <td style="font-size: 16px">ABC2358</td>
            <td style="font-size: 16px">Sociología</td>
            <td style="font-size: 16px">Paula Suárez</td>
            <td>
              <a
                type="button"
                data-toggle="modal"
                data-target="#updateSalaModal"
                ><i class="far fa-edit" style="font-size: 25px"></i
              ></a>
            </td>
          </tr>
          <tr>
            <td style="font-size: 16px">ABC2359</td>
            <td style="font-size: 16px">Derecho</td>
            <td style="font-size: 16px">Fernando Gutiérrez</td>
            <td>
              <a
                type="button"
                data-toggle="modal"
                data-target="#updateSalaModal"
                ><i class="far fa-edit" style="font-size: 25px"></i
              ></a>
            </td>
          </tr>
          <tr>
            <td style="font-size: 16px">EFG10235</td>
            <td style="font-size: 16px">Economía</td>
            <td style="font-size: 16px">Gloria Ortiz</td>
            <td>
              <a
                type="button"
                data-toggle="modal"
                data-target="#updateSalaModal"
                ><i class="far fa-edit" style="font-size: 25px"></i
              ></a>
            </td>
          </tr>
          <tr>
            <td style="font-size: 16px">EFG11235</td>
            <td style="font-size: 16px">Ingeniería Civil</td>
            <td style="font-size: 16px">Ricardo Vargas</td>
            <td>
              <a
                type="button"
                data-toggle="modal"
                data-target="#updateSalaModal"
                ><i class="far fa-edit" style="font-size: 25px"></i
              ></a>
            </td>
          </tr>
          <tr>
            <td style="font-size: 16px">EFG12235</td>
            <td style="font-size: 16px">Ingeniería de Sistemas</td>
            <td style="font-size: 16px">Sara Morales</td>
            <td>
              <a
                type="button"
                data-toggle="modal"
                data-target="#updateSalaModal"
                ><i class="far fa-edit" style="font-size: 25px"></i
              ></a>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>
