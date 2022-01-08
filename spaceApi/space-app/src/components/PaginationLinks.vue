<template>
    <ul :class="cls">
        <li :class="[isInFirstPage() ? 'disabled': '','page-item']">
            <a class="page-link" href="#" tabindex="-1"
            @click="onClickFirstPage">First</a>
        </li>
        <li :class="[isInFirstPage() ? 'disabled': '','page-item']">
            <a class="page-link" href="#" tabindex="-1"
            @click="onClickPreviousPage">«</a>
        </li>
        <li v-for="page in pages" v-bind:key="page.name"
            :class="[isCurrentPage(page.name) ? 'disabled': '','page-item']">
            <a class="page-link"  href="#"
            @click="onClickPage(page.name)">{{page.name}}</a>
        </li>
        <li :class="[isInLastPage() ? 'disabled': '','page-item']">
            <a class="page-link" href="#"
            @click="onClickNextPage">»</a>
        </li>
        <li :class="[isInLastPage() ? 'disabled': '','page-item']">
            <a class="page-link" href="#" tabindex="-1"
            @click="onClickLastPage">Last</a>
        </li>
    </ul>
</template>

<script>
export default {
  name: 'PaginationLinks',
  props: {
    maxVisibleButtons: {
      type: Number,
      required: false,
      default: 5
    },
    current: Number,
    totalPages: Number,
    cls: String
  },
  computed: {
    startPage() {
        // When on the first page
        if (this.current === 1) {
            return 1;
        }

        // When on the last page
        if (this.current === this.totalPages) {
            return this.totalPages - this.maxVisibleButtons;
        }

        // When inbetween
        return this.current - 1
    },
    pages() {
      const range = []

      for (
        let i = this.startPage;
        i <= Math.min(this.startPage + this.maxVisibleButtons - 1, this.totalPages);
        i++
      ) {
        range.push({
          name: i,
          isDisabled: i === this.current
        })
      }

      return range;
    }
  },
  methods: {
    isCurrentPage(page) {
      return this.current === page;
    },
    isInFirstPage() {
      return this.current === 1;
    },
    isInLastPage() {
      return this.current === this.totalPages;
    },
    onClickFirstPage() {
        this.$emit('pagechanged', 1);
    },
    onClickPreviousPage() {
        this.$emit('pagechanged', this.current - 1);
    },
    onClickPage(page) {
        this.$emit('pagechanged', page);
    },
    onClickNextPage() {
        this.$emit('pagechanged', this.current + 1);
    },
    onClickLastPage() {
        this.$emit('pagechanged', this.totalPages);
    }
    }
}
</script>