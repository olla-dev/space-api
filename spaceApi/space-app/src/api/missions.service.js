import GenericError from './errors/generic'
import axios from 'axios'

const apiUrl = 'http://localhost:8000/api'

const MissionService = {

	/**
    * List missions.
    **/
	async getMissions() {
		try {
			const response = await axios.get(apiUrl+'/missions')
			const missions = response.data
			return missions
		} catch (error) {
			throw new GenericError(error.response.status, error.response.data.detail)
		}
	},
}

export default MissionService

export { MissionService, GenericError }

