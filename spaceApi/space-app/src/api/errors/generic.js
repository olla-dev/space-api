export default class GenericError extends Error {

	constructor(code, message) {
		super()
		this.name = this.constructor.name
		this.message = message
		this.code = code
	}

}