import { RedirectInterface } from "./interfaces/redirect_interface";

export class Redirect implements RedirectInterface {
    readonly url : string;

    constructor(url : string) {
        this.url = url;
    }

    run_redirect() : void {
        const url_treated = this.url.split("/")[4];
        const url_base = 'https://www.youtube.com/watch';
        const new_url = `${url_base}?v=${url_treated}`;
        window.location.href = new_url;
    }
}