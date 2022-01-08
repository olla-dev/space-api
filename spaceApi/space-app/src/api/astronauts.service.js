import GenericError from './errors/generic'
import axios from 'axios'

const apiUrl = 'http://localhost:8000/api'

const AstronautService = {

	/**
    * List astronauts.
    **/
	async getAstronauts(page = 1) {
		try {
			const response = await axios.get(apiUrl+'/astronauts', {
				page: page
			})
			const astronauts = response.data
			return astronauts
		} catch (error) {
			throw new GenericError(error.response.status, error.response.data.detail)
		}
	},
}

export default AstronautService

export { AstronautService, GenericError }

