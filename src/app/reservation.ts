export class Reservation {
    room: number 
    checkin_date: string
    checkout_date: string


    constructor(room_id: number, checkin: string, checkout: string){
        this.room = room_id
        this.checkin_date = checkin
        this.checkout_date = checkout
    }
}