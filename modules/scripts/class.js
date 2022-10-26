export class Person {
    constructor(name) {
        this.name = name;
    }

    sayHello(name) {
        console.info(`Hello ${name}, my name is ${this.name}`);
    }

    sayMorning(name) {
        console.info(`Hello ${name}, my name is ${this.name}`);
    }

    sayNight(name) {
        console.info(`Hello ${name}, my name is ${this.name}`);
    }
}