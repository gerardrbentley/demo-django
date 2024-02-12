import http from 'k6/http';
import { check } from 'k6';

let baseUrl = __ENV.SERVICE_URL ? __ENV.SERVICE_URL : "http://localhost:8000"
let users = __ENV.K6_USERS ? __ENV.K6_USERS : 100
let duration = __ENV.K6_DURATION ? __ENV.K6_DURATION : "60s"

export const options = {
    scenarios: {
        contacts: {
            executor: 'constant-vus',
            vus: users,
            duration: duration,
        },
    },
}
export default function () {
    let payload = JSON.stringify({
        "requester": "djan",
        "message": "make it fast 🏎️",
    })

    let parameters = {
        'headers': {
            'Content-Type': 'application/json',
        },
    };

    const res = http.post(baseUrl + '/message', payload, parameters);
    check(res, { 'status was 200': (r) => r.status == 200 });
}
