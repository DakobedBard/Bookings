export class Listing {
    room_id: number
    name: string
    city : string
    state: string
    guest_count: number
    address: string
    bed_count: number
    bath_count: number

    constructor(room_id: number, city: string, state: string, guest_count:number, property_name: string){
        this.room_id = room_id
        this.city = city
        this.state = state
        this.guest_count = guest_count
        this.name = property_name
    }
}