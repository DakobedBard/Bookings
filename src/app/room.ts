export class Room {
    id: number
    name: string
    city : string
    state: string
    guest_count: number
    address: string
    bed_count: number
    bath_count: number
    host: number

    constructor(room_id: number=1, city: string='Detroit', state: string='Michigan', guest_count:number = 1, 
        property_name: string = '8 Mile House', address:string = '8009',host:number = 1){
        this.id = room_id
        this.city = city
        this.state = state
        this.guest_count = guest_count
        this.name = property_name
        this.address = address
        this.host = host
    }
}