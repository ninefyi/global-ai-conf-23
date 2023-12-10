<template>
  <div class="card">
    <h2>{{ title }}</h2>
    <img :src="poster" alt="Movie Poster" class="poster-img" /><br/>
    <p><b>Plot</b>: {{ plot }}
      <hr />
      <b>Year</b>: {{ year }}
      <hr/>
      <b>Score</b>: {{ score }}
    </p>
  </div>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      required: false
    },
    plot: {
      type: String,
      required: false
    },
    year: {
      type: Number,
      required: false
    },
    poster: {
      type: String,
      required: false
    },
    score: {
      type: Number,
      required: false
    }
  }
};
</script>

<style scoped>
.card {
  border: 1px solid #ccc;
  padding: 10px;
  margin-bottom: 10px;
}
b {
  text-decoration: underline;
}
img {
  max-width: 300px;
  max-height: 200px;
}

</style>