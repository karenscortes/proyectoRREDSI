<template>
  <div aria-label="Page navigation">
    <ul class="pagination justify-content-center bg-warnig">
      <li class="page-item" :class="{ disabled: currentPage === 1 }">
        <button
          class="page-link"
          @click="prevPage"
          :disabled="currentPage === 1"
        >
          Anterior
        </button>
      </li>
      <li
        v-for="page in visiblePages"
        :key="page"
        class="page-item rounded m-1"
      >
        <button
          class="page-link rounded-circle"
          @click="changePage(page)"
          :class="{ 'bg-warning text-dark': currentPage == page }"
        >
          {{ page }}
        </button>
      </li>
      <li class="page-item m-1" :class="{ disabled: currentPage === totalPages }">
        <button
          class="page-link"
          @click="nextPage"
        >
          Siguiente
        </button>
      </li>
    </ul>
  </div>
</template>
  
<script setup>
import { ref, computed } from "vue";

const props = defineProps({
  totalPages: {
    type: Number,
    required: true,
  },
});

const emit = defineEmits(["page-changed"]);

const currentPage = ref(1);
const maxVisiblePages = ref(5);

const visiblePages = computed(() => {
  const half = Math.floor(maxVisiblePages.value / 2);
  let start = Math.max(1, currentPage.value - half);
  let end = Math.min(props.totalPages, currentPage.value + half);

  if (currentPage.value <= half) {
    end = Math.min(maxVisiblePages.value, props.totalPages);
  } else if (currentPage.value > props.totalPages - half) {
    start = Math.max(1, props.totalPages - maxVisiblePages.value + 1);
  }

  const pages = [];
  for (let i = start; i <= end; i++) {
    pages.push(i);
  }
  return pages;
});

const changePage = (page) => {
  if (currentPage.value != page) {
    currentPage.value = page;
    emit("page-changed", page);
  }
};

const prevPage = () => {
  if (currentPage.value > 1) {
    changePage(currentPage.value - 1);
  }
};

const nextPage = () => {
  if (currentPage.value < props.totalPages) {
    changePage(currentPage.value + 1);
  }
};
</script>
  
<style scoped>
button{
  border-radius: 20px;
  color: black;

}

button:hover {
  background-color: rgb(255, 255, 255); 
  color:#ffc107; 
}

.pagination {
  display: flex;
  align-items: center;
}

ul {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
}

li {
  margin: 0 5px;
}

button {
  padding: 5px 10px;
}

button.active {
  color: white;
  border-radius: 5px;
}

*::selection {
  background-color: transparent;
}
</style>