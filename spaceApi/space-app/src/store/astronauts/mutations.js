export function fetchAstronautsRequest(state) {
	state.loading = true
	state.fetchError = ''
	state.fetchErrorCode = 0
}

export function fetchAstronautsSuccess(state, payload) {
	state.data = payload
	state.selectedAstronaut = {}
	state.fetchError = ''
	state.fetchErrorCode = 0
	state.loading = false
}

export function fetchAstronautSuccess(state, payload) {
	state.selectedAstronaut = payload
	state.fetchError = ''
	state.fetchErrorCode = 0
	state.loading = false
}

export function fetchAstronautsError(state, { errorCode, errorMessage }) {
	state.loading = false
	state.fetchError = errorMessage
	state.fetchErrorCode = errorCode
}
