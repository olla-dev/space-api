import GenericError from './errors/generic'
import axios from 'axios'

const apiUrl = 'http://localhost:8000/api'

const MissionService = {

	/**
    * List missions.
    **/
	async getMissions(page = 1) {
		try {
			const response = await axios.get(apiUrl+'/missions?page='+page)
			return {
				currentPage: page,
				count: response.data.count,
				totalPages: Math.ceil(response.data.count / 10),
				results: response.data.results
			}
		} catch (error) {
			throw new GenericError(error.response.status, error.response.data.detail)
		}
	},
}

export default MissionService

export { MissionService, GenericError }

