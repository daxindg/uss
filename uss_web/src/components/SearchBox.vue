<template>
    <div style="margin-top: 15px">
        <el-input placeholder="请输入url" v-model="ss" class="input">
            <template #append>
                <el-button @click="onSubmit" type="success" :loading="loading"
                    >生成短链</el-button
                >
            </template>
        </el-input>
        <template v-for="(x, idx) in alerts" :key="idx">
            <el-alert
                :title="x.title"
                class="scc-alert"
                @click="
                    () => {
                        copyToClipboard(x.url);
                        notify({
                            message: x.url,
                            type: 'success',
                            showClose: false,
                            title:'复制成功' 
                        });
                    }
                "
                type="success"
                effect="dark"
                show-icon
            >
            </el-alert>
        </template>
    </div>
</template>

<script lang="ts">
import { defineComponent, ref, Ref } from "vue";
import { isValidUrl } from "../utils/isValidUrl";
import { copyToClipboard } from "../utils/copyToClipboard";

export default defineComponent({
    setup() {
        const ss = ref("");
        const loading = ref(false);
        const alerts: Ref<any[]> = ref([]);
        return {
            ss,
            loading,
            alerts,
        };
    },
    methods: {
        async onSubmit() {
            const url = this.ss;
            if (!isValidUrl(url)) {
                console.log("bad url");
                this.notify({
                    message: "只接受 http(s) 链接",
                    type: "error",
                    showClose: false,
                    title: null
                });
                return;
            }
            const data = new FormData();
            data.append("url", url);
            this.loading = true;
            try {
                const res = await (
                    await fetch("https://daxdg.xyz/s/create", {
                        body: data,
                        method: "post",
                    })
                ).json();
                if (res.ok) {
                    this.alerts.push({
                        url: `https://daxdg.xyz/s/${res.data.hash}`,
                        title: `点击复制 https://daxdg.xyz/s/${res.data.hash} => ${url}`,
                    });
                }
                else {
                   this.notify({
                        type: "error",
                        message: res.err,
                        showClose: false,
                        title: null
                    }); 
                    console.log(res);
                }
            } catch (e) {
                console.log(e);
            }
            this.loading = false;
        },
        copyToClipboard,
        notify(opt:{type:"error"|"info"|"success", message: string, showClose:boolean, title: string | null}) {
            // @ts-ignore
            this.$notify(opt);
        }
    },
});
</script>

<style lang="scss" scoped>
.scc-alert {
    cursor: pointer;
    margin-top: 10px;
}
</style>