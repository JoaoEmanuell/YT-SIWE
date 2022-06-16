class Main {
    url = '';
    constructor() {
        this.url = window.location.href;
    }

    get_url() : string {
        return this.url;
    }

    run() : void {
        if (this.url.search('https://www.youtube.com/shorts') !== -1) {
            const url_treated = this.url.split("/")[4];
            const url_base = 'https://www.youtube.com/watch';
            const new_url = `${url_base}?v=${url_treated}`;
            window.location.replace(new_url);
        }
    }

}

const main = new Main();

const interval = setInterval(() => {
    main.run();
}, 1000);