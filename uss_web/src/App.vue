<template>
    <el-container>
        <el-header> </el-header>
        <el-main>
            <el-row :gutter="10">
                <el-col
                    :xs="{ span: 24, offset: 0 }"
                    :sm="{ span: 20, offset: 2 }"
                    :md="{ span: 16, offset: 4 }"
                    :lg="{ span: 12, offset: 6 }"

                >
                    <search-box />
                </el-col>
            </el-row>
        </el-main>
    </el-container>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import SearchBox from "./components/SearchBox.vue";

export default defineComponent({
    name: "App",
    components: { SearchBox },
    setup() {},
});
</script>

<style lang="scss">
#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
}
</style>
