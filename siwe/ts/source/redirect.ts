import { RedirectInterface } from "./interfaces/redirect_interface";

export class Redirect implements RedirectInterface {
    readonly url : string;

    constructor(url : string) {
        this.url = url;
    }

    run_redirect() : void {
        window.location.href = this.url;
    }
}