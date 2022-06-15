class Main {
    url = '';
    constructor() {
        this.url = window.location.href;
    }

    get_url() : string {
        return this.url;
    }
}

const main = new Main();
window.alert(main.get_url());