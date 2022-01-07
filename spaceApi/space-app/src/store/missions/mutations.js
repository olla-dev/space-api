export function fetchMissionsRequest(state) {
	state.loading = true
	state.fetchError = ''
	state.fetchErrorCode = 0
}

export function fetchMissionsSuccess(state, payload) {
	state.data = payload
	state.selectedMission = {}
	state.fetchError = ''
	state.fetchErrorCode = 0
	state.loading = false
}

export function fetchMissionSuccess(state, payload) {
	state.selectedMission = payload
	state.fetchError = ''
	state.fetchErrorCode = 0
	state.loading = false
}

export function fetchMissionsError(state, { errorCode, errorMessage }) {
	state.loading = false
	state.fetchError = errorMessage
	state.fetchErrorCode = errorCode
}
